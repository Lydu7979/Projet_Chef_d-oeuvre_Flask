from flask import Flask, jsonify, request, render_template, redirect, url_for, send_file, flash
#from utils.MG import data, data_prix, data_pro, day, mg
#from utils.arima import graph_prix_ARIMA1, graph_prix_ARIMA2, graph_pro_ARIMA1, graph_pro_ARIMA2, predict_prix_ARIMA, predict_production_ARIMA
#from utils.data_viz_1 import graph_prix, graph_pro, graph_u
#from utils.lstm import graph_pred_prix_lstm, graph_pred_pro_lstm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_sqlalchemy import SQLAlchemy
import os
import jwt
from time import time
from datetime import datetime
from utils import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never_guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=3, max=40)])
    email = StringField('Email', [validators.Length(min=6, max=100)])
    password = PasswordField('Password', [validators.DataRequired(),
                                          validators.Length(min=6, max=40), 
                                          validators.EqualTo('confirm', message ='Passwords must match')])
    confirm = PasswordField('Confirm Password again')

class  LoginForm(Form):
    email = StringField('Email', validators=[validators.Length(min=6, max=100)])
    password = PasswordField('Password', [validators.DataRequired(),
                                          validators.Length(min=6, max=40), 
                                          validators.EqualTo('confirm', message ='Passwords must match')])
    
    submit = SubmitField('Login')




@app.route("/")
@app.route('/base')
def index():
    return render_template('base.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        return redirect(url_for('application'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("signin.html", form=form)


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
        return redirect(url_for('signin'))
    return render_template('signup.html', form =form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('base'))


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/application')
@login_required
def application():


    return render_template('application.html')