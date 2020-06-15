from application import app
from flask import render_template, request, json, Response, redirect, flash, url_for, session, jsonify
from flask_restplus import Resource

@app.route('/create_customer')
def create_customer():
    return render_template("create_customer.html", title="Create Customer")
