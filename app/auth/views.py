from flask import render_template, redirect, url_for, flash, request
from . import auth
from flask_login import login_user, logout_user, login_required
from ..models import User
from .forms import LoginForm, RegisterForm
from .. import db
from ..email import mail_message


@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    title = "Sign up to Millennial blogs"
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You have Successfully Signed up to the Millennal Blogs Website. Please login to proceed")

        # mail_message("Welcome to MillennialBlogs","email/welcome_user",user.email,user=user)


        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',register_form = form, title = title)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()
    title = "Millennial Blogs login"
    if login_form.validate_on_submit():
        user = User.query.filter_by(username = login_form.username.data).first()
        flash("Welcome to Millenial Blogs")
        if user != None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Wrong Username or Password')
    return render_template('auth/login.html',login_form = login_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

