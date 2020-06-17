from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import Login


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired(), Length(min=5, max=10)])
    submit = SubmitField("Login")


class CustomerForm(FlaskForm):
    customerId = StringField("CUSTOMER ID", validators=[DataRequired(), Length(max=10)])
    customer_name = StringField("CUSTOMER NAME", validators=[DataRequired()])
    age = StringField("AGE", validators=[DataRequired(), Length(max=2)])
    address = StringField("ADDRESS", validators=[DataRequired()])
    state = StringField("STATE")
    submit = SubmitField("REGISTER")

class AccountForm(FlaskForm):
    pass