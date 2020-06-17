import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash
import email_validator


class Login(db.Document):
    first_name = db.StringField(maxlength=510)
    last_name = db.StringField(maxlength=50)
    username = db.StringField(maxlength=50, unique=True)
    password = db.StringField()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)
