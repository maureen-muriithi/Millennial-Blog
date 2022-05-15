from flask import render_template, redirect, url_for, flash, request
from . import auth
from flask_login import login_user, logout_user, login_required
# from ..models import User
from .forms import LoginForm, RegisterForm
# from .. import db
# from ..email import mail_message


@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    title = "Sign up to the Z-Millennial blogs"
    return render_template('auth/register.html',register_form = form, title = title)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    pass

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))