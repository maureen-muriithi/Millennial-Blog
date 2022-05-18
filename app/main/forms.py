from re import sub
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from flask_login import current_user
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from flask_wtf.file import FileField, FileAllowed
from ..models import User

class UpdateProfile(FlaskForm):
    username = StringField('Enter Your Username', validators=[DataRequired()])
    bio = TextAreaField('Write a brief bio about you.',validators = [DataRequired()])
    profile_picture = FileField('profile picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username = username.data).first():
                raise ValidationError("The username has already been taken")

class AddBlog(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    post = TextAreaField('Blog post content',validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField("Post a Comment", validators=[DataRequired()])
    submit = SubmitField("Comment")

class BlogEditForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    post = TextAreaField('Blog content', validators=[DataRequired()])
    submit = SubmitField('Post', validators=[DataRequired()])