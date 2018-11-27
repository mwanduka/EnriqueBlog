from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import Blog_PostForm, Comment_Form
from ..models import Blog, User_comments, Subscription
from .. import db
import markdown2
from flask_login import current_user
from ..email import mail_message


@main.route('/', methods=['GET','POST'])
def index():
    form = Blog_PostForm()

    if form.validate_on_submit():
        title = form.title.data
        Blog_post = form.Blog_post.data

        blog = Blog(blog_name=title, blog_info=Blog_post)

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('.blogpost'))
    posts = Blog.query.order_by(Blog.date_posted.desc()).all()

    return render_template('index.html', form=form, posts=posts)

@main.route('/blogpost/', methods=['GET', 'POST'])
def new_blog():
    form = Blog_PostForm()
    subscribe = Subscription.query.all()
    if form.validate_on_submit():
        title = form.title.data
        Blog_post = form.Blog_post.data

        blog = Blog(blog_name=title, blog_info=Blog_post)

        db.session.add(blog)
        db.session.commit()

        for email in subscribe:
            mail_message("New Blog Alert!!!!",
                         "email/blog_alert", email.email, subscribe=subscribe)
        return redirect(url_for('.index'))
    posts = Blog.query.order_by(Blog.date_posted.desc()).all()
    return render_template('blogpost.html', form=form, posts=posts)


@main.route('/blog/<int:id>', methods=['GET','POST'])
def blog(id):
    '''
    View blog page function that returns the posted blogpost
    '''
    commentform = Comment_Form()


    if commentform.validate_on_submit():
        name = commentform.name.data
        email = commentform.email.data
        comment = commentform.comment.data
        comment = User_comments(username=name, email=email, comment=comment,blogID = id)

        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('.blog',id = id))
    blog = Blog.query.get(id)
    comments = User_comments.query.filter_by(blogID=id).all()
    title = f'{blog.blog_name}'
    return render_template('myposts.html', commentform=commentform, blog=blog,title =title, comments = comments)
