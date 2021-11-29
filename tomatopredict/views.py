from tomatopredict import app
from flask import request, render_template, redirect, url_for, flash
from forms import RegisterForm, LoginForm
from utils import data_viz_1


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

'''@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('base'))'''


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/application')
def application():
    g1 = data_viz_1.graph_u()
    return render_template('application.html', graph = g1)