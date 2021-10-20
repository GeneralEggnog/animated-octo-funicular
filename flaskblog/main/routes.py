from flask import render_template, url_for, flash, redirect, Blueprint, send_file
from flaskblog.main.forms import ContactForm
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def index():
    return render_template("index.html",  title='Home')

@main.route("/about")
def about():
    return render_template("about.html", title='About')

@main.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        sender_email = "kendlewebsite@gmail.com"
        receiver_email = "kendle.lam@gmail.com"
        message = MIMEMultipart("alternative")
        text = MIMEText(
            "<p> Name: " + form.name.data + "<br>"
            "Email: " + form.email.data + "</p>" + 
            form.message.data, "html"
        )
        message["Subject"] = form.subject.data
        message["From"] = sender_email
        message["To"] = receiver_email
        message.attach(text)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
            server.login(sender_email, 'jmsoqxykwomwwpas')
            server.send_message(message)
        flash('Message sent! Thanks for reaching out!', 'success')
        return redirect(url_for('main.contact'))
    return render_template("contact.html", title='Contact', form=form)

@main.route('/.well-known/acme-challenge/5UFmLdsRmujgW77faFCeE86SettuelNiQGpnnetCJSY')
def acme():
    return send_file('static/acme.txt')