from tomatopredict import app
from flask import request, render_template, redirect, url_for, flash
from forms import RegisterForm, LoginForm
from utils import data_viz_1, arima, lstm


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

@app.route('/data-viz', methods = ['GET', 'POST'])
def essai():
    optradio1 = request.form.get('optradio1')
    print(optradio1)
    optradio2 = request.form.get('optradio2')
    print(optradio2)
    optradio3 = request.form.get('optradio3')
    print(optradio3)
    optradio11 = request.form.get('optradio11')
    print(optradio11)
    optradio12 = request.form.get('optradio12')
    print(optradio12)
    optradio13 = request.form.get('optradio13')
    print(optradio13)
    optradio14 = request.form.get('optradio14')
    print(optradio14)
    optradio15 = request.form.get('optradio15')
    print(optradio15)
    optradio16 = request.form.get('optradio16')
    print(optradio16)
    optradio21 = request.form.get('optradio21')
    print(optradio21)
    optradio22 = request.form.get('optradio22')
    print(optradio22)
    if optradio1 == "on":
        g1 = data_viz_1.graph_u()
    elif optradio2 == "on":
        g1 = data_viz_1.graph_prix()
    elif optradio3 == "on":
        g1 = data_viz_1.graph_pro()
    elif optradio11 == "on":
        g1 = arima.predict_prix_ARIMA()
    elif optradio12 == "on":
        g1 = arima.graph_prix_ARIMA1()
    elif optradio13 == "on":
        g1 = arima.graph_prix_ARIMA2()
    elif optradio14 == "on":
        g1 = arima.predict_production_ARIMA()
    elif optradio15 == "on":
        g1 = arima.graph_pro_ARIMA1()
    elif optradio16 == "on":
        g1 = arima.graph_pro_ARIMA2()
    elif optradio21 == "on":
        g1 = lstm.graph_pred_prix_lstm()
    elif optradio22 == "on":
        g1 = lstm.graph_pred_pro_lstm()   
    else:
        return render_template('application.html',graph = "Nok", flag = "Nok")
    return render_template('application.html',graph = g1)