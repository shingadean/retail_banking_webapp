import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash
import email_validator


class Login(db.Document):
    first_name = db.StringField(maxlength=510)
    last_name = db.StringField(maxlength=50)
    username = db.StringField(maxlength=50, unique=True)
    password = db.StringField()



class Customer(db.Document):
    customerId = db.StringField(maxlength=10)
    customer_name = db.StringField(maxlength=15)
    age = db.StringField(maxlength=2)
    address = db.StringField(maxlength=100)
    state = db.StringField()
