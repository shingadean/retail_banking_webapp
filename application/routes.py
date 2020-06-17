from application import app
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from flask_restplus import Resource
from application.data_country import states_list
from application.forms import LoginForm, CustomerForm
from application.models import Login, Customer


@app.route('/home')
def home():
    return render_template('home.html', home=True)


@app.route('/', methods=["GET", "POST"])
@app.route('/login',methods=["GET", "POST"])
def login():
    if session.get('username'):
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        login_form = Login.objects(username=username).first()
        if login_form and password:
            flash(f"{login_form.first_name}, You are Logged IN", 'success')
            session['username'] = login_form.username
            session['first_name'] = login_form.first_name
            return redirect(url_for("home"))
        else:
            flash("Sorry, something went wrong.", "danger")
    return render_template("login.html", title="Login", form=form, login=True)


@app.route('/create_customer', methods=['GET','POST'])
def create_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        ssn_id = form.customerId.data
        name = form.customer_name.data
        age = form.age.data
        address = form.address.data
        state= form.state.data
        if state is not None:

            customer = Customer(customerId=ssn_id, customer_name=name, age=age, address=address, state=state)
            customer.save()
            flash("CUSTOMER CREATED SUCCESSFULLY", "success")
            return redirect(url_for('create_customer'))
        else:
            flash("Sorry, Something went wrong","danger")

    return render_template("create_customer.html", title="Create Customer",
                           customer_management=True, form=form)


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

@app.route('/logout')
def logout():
    session['username'] = False
    session.pop('first_name', None)
    flash("You are logged out", 'alert')
    return redirect(url_for('home'))