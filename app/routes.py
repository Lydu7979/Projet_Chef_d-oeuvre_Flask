from app.forms import LoginForm, RegisterForm, ResetPasswordForm, NewPasswordForm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,  jsonify, request, render_template, redirect, url_for, send_file
from flask_login import current_user, login_user, logout_user, login_required
#logging.basicConfig(filename='demo.log')
#logging.debug('This message should go to the log file')
from app import app2, db, bcrypt
from app.models import UserModel
from Base_données.DBMongo import get_client_mongodb
import dns
import pymongo
import pandas as pd
import dns
from Sécurité.Safe import modi, verif
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt



app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home_page():
	return render_template('home.html')

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('base.html')


@app.route('/login')
def login():
    
	return render_template("login.html", title='Sign In')

@app.route('/connection')
def connet():
    return render_template('register.html', methods=["GET", "POST"])

@app.route('/Graphiques')
@login_required
def graphi():
    return render_template("graph.html", title='Graphs')

@app.route('/nbj')
@login_required
def nbday():
    return render_template('nbj.html')
 
@app.route('/dataj/', methods = ['POST', 'GET'])
@login_required
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('dataj.html',form_data = form_data)

@app.route('/Arima_prediction')
@login_required
def arima():
    return render_template("arima.html", title='Prediction_ARIMA')
    
@app.route('/LSTM_prediction')
@login_required
def lstm():
    return render_template("lstm.html", title='Prediction_LSTM')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'), title='Sign out')
    


