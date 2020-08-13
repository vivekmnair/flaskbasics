from flask_login import login_user, current_user, logout_user, login_required
from flask_login import UserMixin
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy 
from newproject import db
from newproject import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120),nullable=False)
    image = db.Column(db.String(120))
    posts = db.relationship('Post', backref='author', lazy=True)
    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    
    def __repr__(self):
        return "Post('{self.title}', '{self.date_posted}')"

class Linkpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    linktitle = db.Column(db.String(100), nullable=False)
    newdate_posted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    newcontent = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    
    def __repr__(self):
        return "Linkpost('{self.linktitle}', '{self.newdate_posted}')"
