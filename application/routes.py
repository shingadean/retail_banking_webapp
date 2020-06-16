from application import app
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from flask_restplus import Resource
from application.data_country import states_list



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', home=True)


@app.route('/login')
def login():
    return render_template("login.html", login=True, title="LOGIN")

@app.route('/create_customer')
def create_customer():
    return render_template("create_customer.html", title="Create Customer", states=states_list)

@app.route('/update_customer')
def update_customer():
    return render_template("update_customer.html", title="Update Customer")


@app.route('/delete_account')
def delete_account():
    return render_template("delete_account.html", title="Delete Account")

@app.route('/create_account')
def create_account():
    return render_template("create_account.html", title="Create Account")

@app.route('/deposit_amount')
def deposit_amount():
    return render_template("deposit_amount.html", title="Cash Deposit")


@app.route('/withdraw_amount')
def withdraw_amount():
    return render_template("withdraw_amount.html", title="Withdraw Cash")

