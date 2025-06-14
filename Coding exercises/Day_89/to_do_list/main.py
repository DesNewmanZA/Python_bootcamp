# Import needed modules
from datetime import date, datetime
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, Date, func
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateField, TextAreaField
from wtforms.validators import DataRequired, Optional


# Create database
class Base(DeclarativeBase):
    pass


# Initialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SECRET_KEY'] = 'my_secret_key'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
bootstrap = Bootstrap5(app)


# Task table configuration
class Task(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    logged_date: Mapped[date] = mapped_column(Date, nullable=False, default=func.current_date())
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(10000), nullable=True)
    due_date: Mapped[date] = mapped_column(Date, nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean, nullable=False)

    # Function to convert data into dictionary format
    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


# Initialize database
with app.app_context():
    db.create_all()


# Make a class for the task form
class TaskForm(FlaskForm):
    name = StringField('Task name', validators=[DataRequired()])
    description = TextAreaField('Task description')
    due_date = DateField('Due date', format='%Y-%m-%d', validators=[Optional()])
    completed = BooleanField('Completed?')
    submit = SubmitField("Add task")


# Define home page
@app.route("/")
def display_home():
    sort_by = request.args.get("sort_by", "due_date")
    status_filter = request.args.get("status_filter", "all")
    query = Task.query

    if status_filter == "completed":
        query = query.filter(Task.completed.is_(True))
    elif status_filter == "pending":
        query = query.filter(Task.completed.is_(False))

    if sort_by == "due_date":
        query = query.order_by(Task.due_date.asc().nulls_last())
    elif sort_by == "name":
        query = query.order_by(Task.name.asc())
    elif sort_by == "completed":
        query = query.order_by(Task.completed.asc(), Task.due_date.asc().nulls_last())
    else:
        query = query.order_by(Task.due_date.asc().nulls_last())

    all_tasks = query.all()
    return render_template("index.html", tasks=all_tasks, sort_by=sort_by, status_filter=status_filter)


# Define add task page
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(
            name=form.name.data,
            description=form.description.data,
            due_date=form.due_date.data,
            completed=form.completed.data or False
        )
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully!", "success")
        return redirect((url_for('display_home', sort_by=request.args.get('sort_by', 'due_date'),
                                 status_filter=request.args.get('status_filter', 'all'))))
    return render_template("add_task.html", form=form)


# Make routine marking a task as complete
@app.route("/toggle_complete/<int:id>", methods=["POST"])
def toggle_complete(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('display_home', sort_by=request.args.get('sort_by', 'due_date'),
                            status_filter=request.args.get('status_filter', 'all')))


# Routine to delete a task
@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete_task(id):
    task_to_delete = Task.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('display_home', sort_by=request.args.get('sort_by', 'due_date'),
                                status_filter=request.args.get('status_filter', 'all')))
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting task: {str(e)}', 'danger')
        return redirect(url_for('display_home', sort_by=request.args.get('sort_by', 'due_date'),
                                status_filter=request.args.get('status_filter', 'all')))


# Routine to edit task
@app.route('/edit_task/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = Task.query.get_or_404(id)

    if request.method == 'POST':
        task.name = request.form['name']
        task.description = request.form.get('description')
        due_date_str = request.form.get('due_date')
        if due_date_str:
            try:
                task.due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            except ValueError:
                flash('Invalid date format. Use YYYY-MM-DD.', 'danger')
                return redirect(url_for('edit_task', id=id))
        else:
            task.due_date = None

        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('display_home', sort_by=request.args.get('sort_by', 'due_date'),
                                status_filter=request.args.get('status_filter', 'all')))

    return render_template('edit_task.html', task=task)


# Run website
if __name__ == '__main__':
    app.run(debug=True)
