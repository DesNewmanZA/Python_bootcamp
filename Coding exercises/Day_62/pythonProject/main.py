# Import needed modules
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL
import csv


# Initiate Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# Make a class for the form
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Location URL', validators=[URL()])
    open = StringField('Opening time', validators=[DataRequired()])
    close = StringField('Closing time', validators=[DataRequired()])
    coffee = SelectField('Coffee rating',
                         choices=[('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'),
                                    ('☕☕☕☕', '☕☕☕☕'), ('☕☕☕☕☕', '☕☕☕☕☕')],
                         validators=[DataRequired()])
    wifi = SelectField('Wifi rating',
                       choices=[('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'),
                                ('💪💪💪💪', '💪💪💪💪'), ('💪💪💪💪💪', '💪💪💪💪💪')],
                       validators=[DataRequired()])
    power = SelectField('Power rating',
                        choices=[('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'),
                                 ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')],
                        validators=[DataRequired()])

    submit = SubmitField('Submit', render_kw={"class": "btn btn-warning mt-3"})


# Define home page
@app.route("/")
def home():
    return render_template("index.html")


# Define a page to add a new row into the cafe data
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


# Define a page that shows all the Cafes listed in the CSV
@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


# Run the flask app
if __name__ == '__main__':
    app.run(debug=True)
