import email
from enum import unique
# from app import db,login_manager
from datetime import datetime
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash, check_password_hash

# class User(UserMixin, db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(255), unique = True, nullable = False)
#     email = db.Column(db.String(255), unique = True, nullable = False)
#     secure_password = db.Column(db.String(255), nullable = False)
#     bio = db.Column(db.String(255))
#     profile_pic_path = db.Column(db.String())
#     blogs = db.relationship('Blog', backref='user', lazy='dynamic')




# class Blog(UserMixin, db.Model):
#     __tablename__ = 'blogs'
#     id = db.Column(db.Integer, primary_key = True)

