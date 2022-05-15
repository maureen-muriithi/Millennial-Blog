import email 
from app import db
# login_manager
from datetime import datetime
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), unique = True, nullable = False)
    email = db.Column(db.String(255), unique = True, nullable = False)
    secure_password = db.Column(db.String(255), nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blogs = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.secure_password,password)

    def __repr__(self):
        return f'User {self.username}'




# class Blog(db.Model):
#     __tablename__ = 'blogs'
#     id = db.Column(db.Integer, primary_key = True)

# class Comment(db.Model):
#     __tablename__ = 'comments'
#     id = db.column(db.integer, primary_key = True)

