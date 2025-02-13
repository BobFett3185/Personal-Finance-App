# basic setup for a flask app

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager
# create the database in this file

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'Pakistan#1'# encrypts cookies... something like that
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views 
    from .auth import auth 
    app.register_blueprint(views, utr_prefix = '/')
    app.register_blueprint(auth, utr_prefix = '/')
    # registering blueprints

    from .models import User
    create_database(app)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    # This chunk of code checks for the user id 


    return app

#def create_database(app):
#    if not path.exists('PFW/' + DB_NAME):
  #      db.create_all(app = app)
  #      print("created database")


# this function creates the database and is called in the previous function
def create_database(app):
    try:
        with app.app_context():
            if not path.exists(DB_NAME):
                db.create_all()
                print("Database created")
                print(f"Database path: {os.path.abspath(DB_NAME)}")
    except Exception as e:
        print(f"Error creating database: {e}")