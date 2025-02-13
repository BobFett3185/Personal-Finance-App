#Database models are on this py file 
# this is the setup for the database for collecting user accounts 

from . import db 
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)   # this is the unique identifier to differentiate every object
    email = db.Column(db.String(150), unique = True) # column for emails, max email length of 150 and email can't be already in use
    password = db.Column(db.String(150)) # column for passwords 
    firstName = db.Column(db.String(150))