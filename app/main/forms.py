from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class Blog_PostForm(FlaskForm):

    title = StringField('Blog Title', validators=[Required()])
    Blog_post = TextAreaField('Blog Content')
    submit = SubmitField('Submit')

class Comment_Form(FlaskForm):

    name = StringField('Your Name', validators=[Required()])
    email = StringField('Your Email', validators=[Required()])
    comment = TextAreaField('Enter Comment')
    submit = SubmitField('Submit')
