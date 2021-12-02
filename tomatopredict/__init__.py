
from flask import Flask, redirect, render_template, flash, url_for
import flask_monitoringdashboard as dashboard
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never_guess'

import views

class Baseconfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')