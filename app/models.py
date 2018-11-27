from . import db, admin, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__='blogger'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, index=True)
    password_hash = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.name}'




class Blog(db.Model):
    __tablename__='blog'
    id = db.Column(db.Integer, primary_key=True)
    blog_name = db.Column(db.String(100))
    blog_info = db.Column(db.String(1000000))
    date_posted = db.Column(db.Time, default=datetime.utcnow())
    comments = db.relationship('User_comments', backref='comments', lazy="dynamic")

    def __repr__(self):
        return f'User {self.blog_name}'

class User_comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    comment = db.Column(db.String(1000))
    blogID = db.Column(db.Integer, db.ForeignKey('blog.id'))

    def __repr__(self):
        return f'User {self.username}'

class Subscription(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return f'User {self.name}'


admin.add_view(ModelView(User, db.session))

admin.add_view(ModelView(Blog, db.session))

admin.add_view(ModelView(User_comments, db.session))

admin.add_view(ModelView(Subscription, db.session))
