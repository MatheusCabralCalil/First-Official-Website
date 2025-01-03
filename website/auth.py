from flask import Blueprint, render_template, request, flash, redirect, url_for
#Importing "request" allow us to get the information from login and sign up page   
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash 
#hash makes so that we never store passwords as plain text. It gives much more security
from . import db
#access all information about the logged in user
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/logout')
#makes sure that the user is unable to acess "def lougout" root without being logged in
def logout():
    logout_user()
    return redirect(url_for('auth.home'))

@auth.route('/home')
def home():
    print(f"Is user logged in? {current_user.is_authenticated}")
    return render_template("home.html")

@auth.route('/login', methods=['GET', 'POST']) 
# Inside the square bracket, we are stating which methods the URL can accept(detault is only GET request)
def login():
    if request.method == 'POST':
        email= request.form.get('email')
        password = request.form.get('password')
        #looks for specific entry/user in the database. 'first' means that will give us the first answer
        user = User.query.filter_by(email=email).first()
        if user:
            #checks if the password is correct and if it is, logs in
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                #IMPORTANT. Keeps the user logged in even if they leave website 
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("login.html")

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1').strip()
        password2 = request.form.get('password2').strip()

        #check if user already exists
        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('Email alreay exists', category='error')
            return redirect(url_for('auth.login'))
            #return render_template("login.html")
        elif len(email) <4:
            flash('Email must be greater than 3 characters.', category='error')
            #category can be named whatever I want
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Passwords dont match.', category='error')
        elif len(password1) <7:
            flash('Password is too short. Must be at least 7 characters.', category='error')
        else:
            #if all conditions are met, adds user to database
            new_user = User(email=email, first_name = first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            #adds user to database
            db.session.add(new_user)
            #updates databse
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            #Redirects user back to home. 'views.home' is where we are redirecting the user to. Calls the function in views.py
            return redirect(url_for('views.home'))
        
    return render_template("sign_up.html")




@auth.route('/option1_1')
@login_required
def option1_1():
    return render_template('/options/option 1/option1_1.html')

@auth.route('/option1_2')
def option1_2():
    return render_template('/options/option 1/option1_2.html')

@auth.route('/option1_2_1')
def option1_2_1():
    return render_template('/options/option 1/option1_2_1.html')

@auth.route('/option1_4_1')
def option1_4_1():
    return render_template('/options/option 1/option1_4_1.html')

@auth.route('/option1_3')
def option1_3():
    return render_template('/options/option 1/option1_3.html')


@auth.route('/option2_1')
@login_required
def option2_1():
    return render_template('/options/option 2/option2_1.html')

@auth.route('/option2_2')
def option2_2():
    return render_template('/options/option 2/option2_2.html')

@auth.route('/option2_3')
def option2_3():
    return render_template('/options/option 2/option2_3.html')


@auth.route('/option3_1')
@login_required
def option3_1():
    return render_template('/options/option 3/option3_1.html')

@auth.route('/option3_2')
def option3_2():
    return render_template('/options/option 3/option3_2.html')

@auth.route('/option3_3')
def option3_3():
    return render_template('/options/option 3/option3_3.html')

@auth.route('/option1_4')
def option1_4():
    return render_template('/options/option 1/option1_4.html')

@auth.route('/option2_4')
def option2_4():
    return render_template('/options/option 2/option2_4.html')

@auth.route('/option3_4')
def option3_4():
    return render_template('/options/option 3/option3_4.html')

@auth.route('/option1_5')
def option1_5():
    return render_template('/options/option 1/option1_5.html')

@auth.route('/option2_5')
def option2_5():
    return render_template('/options/option 2/option2_5.html')

@auth.route('/option3_5')
def option3_5():
    return render_template('/options/option 3/option3_5.html')
