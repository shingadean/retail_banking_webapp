from application import app
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from flask_restplus import Resource
from application.data_country import states_list
from application.forms import LoginForm
from application.models import Login


@app.route('/home')
def home():
    return render_template('home.html', home=True)


@app.route('/', methods=["GET", "POST"])
@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data

        login_form = Login.objects(username=username).first()
        if login_form and password:
            flash("You are Logged IN")
            return redirect("/home")
    else:
        flash("Sorry, something went wrong.", "danger")

    return render_template("login.html", title="Login", form=form, login=True)


@app.route('/create_customer')
def create_customer():
    return render_template("create_customer.html", title="Create Customer", states=states_list,
                           customer_management=True)


@app.route('/update_customer')
def update_customer():
    return render_template("update_customer.html", title="Update Customer", customer_management=True)


@app.route('/delete_account')
def delete_account():
    return render_template("delete_account.html", title="Delete Account", account_management=True)


@app.route('/create_account')
def create_account():
    return render_template("create_account.html", title="Create Account", account_management=True)


@app.route('/deposit_amount')
def deposit_amount():
    return render_template("deposit_amount.html", title="Cash Deposit", account_operation=True)


@app.route('/withdraw_amount')
def withdraw_amount():
    return render_template("withdraw_amount.html", title="Withdraw Cash", account_operation=True)
@app.route('/account_status')
def account_status():
    return render_template("account_status.html", title="account Status")


