from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint("views", __name__) # defining a blueprint for views 

@views.route('/') # home page route
@login_required # can't access homepage without logged in
def home():
    return render_template("home.html", user = current_user)  # this renders the template from home.html, which is an extension of base

# you can assign the user via the python module so you now can access the user in the html file

