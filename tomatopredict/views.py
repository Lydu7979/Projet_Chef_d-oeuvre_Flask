from tomatopredict import app, get_db
from flask import request, render_template, redirect, url_for, flash
from forms import RegisterForm, LoginForm
from utils import data_viz_1
from utils.MG import mg
from utils.arima import prix_a, pro_a

@app.route("/")
@app.route('/base')
def index():
    cur = get_db().cursor()
    print(cur)
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
    nbd = request.form.get('nbd')
    tabprixa = prix_a(int(nbd))
    print(tabprixa)
    tabproa = pro_a(int(nbd))
    print(tabproa)
    optradio1 = request.form.get('optradio1')
    print(optradio1)
    optradio2 = request.form.get('optradio2')
    print(optradio2)
    optradio3 = request.form.get('optradio3')
    print(optradio3)
    if optradio1 == "on":
        g1 = data_viz_1.graph_u()
    elif optradio2 == "on":
        g1 = data_viz_1.graph_prix()
    elif optradio3 == "on":
        g1 = data_viz_1.graph_pro()   
    else:
        return render_template('application.html', graph = "Nok", flag = "Nok")
    return render_template('application.html', graph = g1, table_prix = tabprixa.to_html() , table_prod = tabproa.to_html())