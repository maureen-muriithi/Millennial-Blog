from . import main
from flask import render_template,request, redirect, url_for

@main.route('/')
def index():

    title = 'Welcome to Millennial Blogs'
    message = 'I love Python'

    return render_template('index.html', title=title, )

@main.route('/profile')
def profile():

    title = 'your profile page'

    return render_template('profile/profile.html', title=title)

@main.route('/blogs')
def blogs():

    title = 'Welcome to Z-Millenial Blogs'

    return render_template('blogs.html', title=title)