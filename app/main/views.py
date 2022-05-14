from . import main
from flask import render_template

@main.route('/')
def index():

    title = 'Welcome to Millennial Blogs'
    message = 'I love Python'

    return render_template('index.html', title=title, message = message)