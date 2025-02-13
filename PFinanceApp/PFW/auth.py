from flask import Blueprint, render_template, request , flash , redirect, url_for
from  PFW.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint("auth", __name__) # defining a blueprint for auth



@auth.route('/login', methods = ['GET', 'POST']) #login page route

# this is all just to check credentials to get a login for your account. 
# it first finds the email that is inputted in the form and searches for it in the db
# then it checks if the password is correct for that 
def login():
    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()
        if user.password is not None:
            
            print (password)
        if password is not None:
            print ("password is here")

        if user and user.password:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category = 'success')
                login_user(user, remember= True)
                return redirect (url_for('views.home'))
            else:
                flash('Incorrect Password, please try again', category = 'error')
        else:       flash("Email doesn't exist, please try again", category = 'error')
  
    return render_template("login.html", user = current_user)


@auth.route('/logout') #logout page route
@login_required # can't access this unless someone is logged in
def logout():
    logout_user()
    return redirect(url_for("auth.login"))



@auth.route('/sign-up',methods = ['GET', 'POST'])   #sign up page route
def signUp():
    if request.method  == 'POST':
        # get requests for all the sign up attributes you need to fill out
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email = email).first()

# checking if all the entered information is valid
# using message flashing when error in login fields, to ,let the user know if something is wrong

        if user:
            flash('Email already exists', category = 'error')
        elif len(email) < 4 :
            flash('Email must be greater than 3 characters', category = 'error') 
        elif len(firstName) < 2:
            flash('Your first name must be greater than 1 character', category  = 'error')
        elif len(password1)< 7:
            flash('Password length must be greater than 6 characters', category  = 'error')
        elif password1!= password2:
            flash('Your password do not match, please try again', category  = 'error') 
        else:
            new_user = User(email = email, firstName = firstName, password = generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember= True)
            flash('Your account was created', category  = 'success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html", user = current_user)

