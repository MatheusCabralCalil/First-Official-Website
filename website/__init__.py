from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager 

#creating database
db = SQLAlchemy()
DB_NAME = 'database.db'

#defining app
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'personalproject'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth


    #Register the blueprint
    #url_prefix is stating what need to appear in order to reach a page
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    #what will the user see if they are not logged out
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #Telling flask how we load our user
    @login_manager.user_loader
    def load_user(id):
        #.get looks for the primery key(telling flask what  user we are looking for, identifying by ID)
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():  # Use the app context
            db.create_all()
        print('Created Database!')