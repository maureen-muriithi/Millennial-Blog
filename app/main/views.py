from . import main
from flask import render_template,request, redirect, url_for, abort
from flask_login import login_required
from ..models import User, Blog
from .forms import UpdateProfile, AddBlog
from .. import db

@main.route('/')
def index():

    title = 'Welcome to Millennial Blogs'

    return render_template('index.html', title=title, )

@main.route('/user/<username>')
@login_required
def profile(username):

    title = 'your profile page'
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", title = title, user = user)

@main.route('/user/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    update_form = UpdateProfile()

    if update_form.validate_on_submit():
        user.bio = update_form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',username=user.username))

    return render_template('profile/update.html',update_form =update_form)

@main.route('/blogs')
def blogs():

    title = 'Welcome to Z-Millenial Blogs'

    return render_template('blogs.html', title=title)