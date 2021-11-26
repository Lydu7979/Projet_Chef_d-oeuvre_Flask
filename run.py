from flask import Flask, jsonify, request, render_template, redirect, url_for, send_file, flash
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField
from flask_login import current_user, login_user, logout_user, login_required 


app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never_guess'

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
    remember_me = BooleanField('Remember Me')
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