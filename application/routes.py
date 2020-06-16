from application import app
from flask import render_template, request, json, Response, redirect, flash, url_for, session, jsonify
from flask_restplus import Resource
from application.data_country import states_list

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_customer')
def create_customer():
    return render_template("create_customer.html", title="Create Customer", states=states_list)

@app.route('/close_account')
def close_account():
    return render_template("close account.html")


@app.route('/delete_account')
def delete_account():
    return render_template("delete_account.html")

@app.route('/login')
def login():
    return render_template("login.html")