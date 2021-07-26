from flask import render_template, url_for
from flaskblog import app

posts = [
    {
        'title':'How to climb to Challenger',
        'date_posted':'7/26/21',
        'content':'This is a test post.',
    },
    {
        'title':'Riven Animation Cancels',
        'date_posted':'4/15/08',
        'content':'This is a guide on the basic animation cancels for Riven.',
    }
]


@app.route("/")
@app.route("/home")
def index():
    home_image = url_for('static', filename='homepic.jpg')
    return render_template("index.html", home_image = home_image, title='Home')

@app.route("/about")
def about():
    about_image = url_for('static', filename='about_image.jpg')
    return render_template("about.html", about_image = about_image, title='About')

@app.route("/blog")
def blog():
    return render_template("blog.html", posts = posts, title='Blog')