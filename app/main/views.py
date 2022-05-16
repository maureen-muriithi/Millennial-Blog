from . import main
from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from ..models import User, Blog, Comment, Subscribers, Upvote, Downvote
from .forms import UpdateProfile, AddBlog, CommentForm
from .. import db, photos
from ..request import get_quote
from ..email import mail_message
from datetime import datetime

@main.route('/')
def index():

    title = 'Welcome to Millennial Blogs'
    # date = Blog.query.get("date_posted")
    blogs = Blog.query.all()
    random_quote = get_quote()

    return render_template('index.html', title=title, blogs=blogs, quote=random_quote )

@main.route('/user/<username>')
@login_required
def profile(username):

    title = 'your profile page'
    user = User.query.filter_by(username = username).first()
    user_id = current_user._get_current_object().id
    posts = Blog.query.filter_by(user_id = user_id).all()
    image = url_for('static', filename='photos/' + current_user.profile_pic_path)

    if user is None:
        abort(404)

    return render_template("profile/profile.html", title = title, user = user, posts=posts, image=image)

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

    return render_template('profile/update_profile.html',update_form =update_form)

@main.route('/user/<username>/update/pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',username=username))

@main.route('/blog/<int:blog_id>', methods = ['GET'])

def blog(blog_id):
    title = 'Welcome to Millennial Blogs'
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
   
    return render_template('blog.html', blog = blog,all_comments=all_comments, title = title, form=form)


@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_blog():
    form = AddBlog()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        user_id = current_user
        new_blog_object = Blog(post=post,user_id=current_user._get_current_object().id,title=title)
        new_blog_object.save_blog()
        return redirect(url_for('main.index'))
        
    return render_template('new_blog.html', form = form)

@main.route('/like/<int:id>', methods=['POST', 'GET'])
@login_required
def like(id):
    blog = Blog.query.get(id)
    upvote = Upvote(blog=blog, upvote=1)
    upvote.save()
    return redirect(url_for('main.index'))


@main.route('/dislike/<int:id>', methods=['GET', 'POST'])
@login_required
def dislike(id):
    blog = Blog.query.get(id)
    downvote = Downvote(blog=blog, downvote=1)
    downvote.save()
    return redirect(url_for('main.index' ))

@main.route('/comment/<int:blog_id>', methods = ['POST','GET'])
@login_required
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment, user_id = user_id, blog_id = blog_id)
        new_comment.save()
        return redirect(url_for('.comment', blog_id = blog_id))
    return render_template('comment.html', form =form, blog = blog, all_comments=all_comments)

@main.route("/blog/<int:id>/<int:comment_id>/delete")
def delete_comment(id, comment_id):
    blog = Blog.query.filter_by(id = id).first()
    comment = Comment.query.filter_by(id = comment_id).first()
    db.session.remove()
    db.session.commit()
    return redirect(url_for("main.comment", blog_id = blog.id))



