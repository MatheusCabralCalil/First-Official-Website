# . = website. In other words, this is the same as "from website import db"
from . import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    #the number 150 is the maximum length. "Unique=True" make is impossible for another user to have the same email as another user
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))