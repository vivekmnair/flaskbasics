from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import os
from random import randint
from datetime import datetime

from flask_login import login_user, current_user, logout_user, login_required
from flask_login import UserMixin
from flask_login import LoginManager
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mysite.db"
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

UPLOAD_FOLDER = 'static/upload'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
from newproject import routes