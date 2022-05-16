import email
from email.policy import default 
from app import db,login_manager
from datetime import datetime
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), unique = True, nullable = False)
    email = db.Column(db.String(255), unique = True, nullable = False)
    secure_password = db.Column(db.String(255), nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(), nullable=False, default='default.jpg')
    blogs = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvote = db.relationship('Upvote', backref='user', lazy='dynamic')
    downvote = db.relationship('Downvote', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.secure_password,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable=False)
    post = db.Column(db.Text(), nullable = False)
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comment = db.relationship('Comment', backref='blog', lazy='dynamic')
    upvote = db.relationship('Upvote', backref='blog', lazy='dynamic')
    downvote = db.relationship('Downvote', backref='blog', lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls,id):
        blogs = Blog.query.filter_by(user_id = id).order_by(Blog.posted_at.desc()).all()
        return blogs
    
    def __repr__(self):
        return f"Blog('{self.title}', '{self.date_posted}')"



class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    comment = db.Column(db.String())
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(blog_id=id).all()

        return comments


    def __repr__(self):
        return f'Comment {self.comment}'


class Subscribers(db.Model):
    __tablename__ = "subscribers"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, index = True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'


class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key=True)
    upvote = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    

    def save_upvote(self):
        db.session.add(self)
        db.session.commit()

    def upvote(cls, id):
        upvote_blog = Upvote(user=current_user, blog_id=id)
        upvote_blog.save()

    @classmethod
    def query_upvotes(cls, id):
        upvote = Upvote.query.filter_by(blog_id=id).all()
        return upvote

    @classmethod
    def all_upvotes(cls):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.blog_id}'

class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key=True)
    downvote = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    def downvote(cls, id):
        downvote_blog = Downvote(user=current_user, blog_id=id)
        downvote_blog.save()

    @classmethod
    def query_downvotes(cls, id):
        downvote = Downvote.query.filter_by(blog_id=id).all()
        return downvote

    @classmethod
    def all_downvotes(cls):
        downvote = Downvote.query.order_by('id').all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.blog_id}'

class Quote:
    """
    Class for quotes consumed from API
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote
