# Import needed modules
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

# Initialize flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecretKey'
Bootstrap5(app)
ckeditor = CKEditor(app)
app.config['CKEDITOR_CONFIG'] = {'versionCheck': False}


# Create database
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Configure and initialize table of blog posts
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # Function to convert data into dictionary format
    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


# Define a new blog post form class
class BlogPostForm(FlaskForm):
    title = StringField('Blog post title')
    subtitle = StringField('Blog post subtitle')
    author = StringField('Your name')
    img_url = StringField('Blog image URL')
    body = CKEditorField('Body')
    submit = SubmitField('Submit')


with app.app_context():
    db.create_all()


# Define home page
@app.route('/')
def get_all_posts():
    blog_posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=blog_posts)


# Define blog post page
@app.route('/post/<post_id>')
def show_post(post_id):
    # Refactored to improve
    # requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# Define add new blog post page
@app.route('/new-post', methods=["GET", "POST"])
def add_new_post():
    form = BlogPostForm()
    if request.method == "POST":
        new_post = BlogPost(
            title=request.form.get("title"),
            subtitle=request.form.get("subtitle"),
            date=datetime.now().strftime("%B %d, %Y"),
            body=request.form.get("body"),
            author=request.form.get("author"),
            img_url=request.form.get("img_url"),
        )

        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form, title="New Post")


@app.route('/edit-post/<post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    form = BlogPostForm(title=requested_post.title,
                        subtitle=requested_post.subtitle,
                        img_url=requested_post.img_url,
                        author=requested_post.author,
                        body=requested_post.body)

    if request.method == "POST" and form.validate_on_submit():
        requested_post.title = form.title.data
        requested_post.subtitle = form.subtitle.data
        requested_post.img_url = form.img_url.data
        requested_post.author = form.author.data
        requested_post.body = form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=requested_post.id))

    return render_template("make-post.html", form=form, title="Edit Post")


@app.route('/delete/<post_id>', methods=["GET", "DELETE"])
def delete_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    db.session.delete(requested_post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Render about page
@app.route("/about")
def about():
    return render_template("about.html")


# Render contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
