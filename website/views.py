from flask import Blueprint,render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

#Showing what user will see after putting something in front of URL
@views.route('/')
def home():
    return render_template('base.html')