from flask import render_template, url_for, flash, redirect, Blueprint
from flaskblog.users.forms import AdminForm
from flaskblog.models import User
from flaskblog import users, bcrypt
from flask_login import login_user, logout_user

users = Blueprint('users', __name__)

@users.route("/admin", methods=["GET", "POST"])
def admin():
    form = AdminForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You have been logged in!', 'success')
            return redirect(url_for('posts.blog'))
        else: 
            flash('Incorrect credentials', 'danger')
            return redirect(url_for('users.admin'))
    return render_template ('admin_login.html', title = 'Admin', form = form)

@users.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out', 'danger')
    return redirect(url_for('main.index'))