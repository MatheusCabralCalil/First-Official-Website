from flask import Blueprint, render_template, request, flash, redirect, url_for
#Importing "request" allow us to get the information from login and sign up page   
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash 
#hash makes so that we never store passwords as plain text. It gives much more security
from . import db
#access all information about the logged in user
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/')
def home_1():
    return render_template('index
    .html')

@auth.route('/logout')
#makes sure that the user is unable to acess "def lougout" root without being logged in
def logout():
    logout_user()
    return redirect(url_for('auth.home_1'))

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
            flash("Email already exists", category="error")
            return redirect(url_for("auth.sign_up"))
        
        if len(first_name) < 4:
            flash("Password is too short.", category="error")
            return redirect(url_for("auth.sign_up"))
 
        if len(password1) < 4:
            flash("Password is too short.", category="error")
            return redirect(url_for("auth.sign_up"))

        if password1 != password2:
            flash("Passwords don't match.", category="error")
            return redirect(url_for("auth.sign_up"))

        try:
            new_user = User(
                email=email,
                first_name=first_name,
                password=generate_password_hash(password1, method="pbkdf2:sha256"),
            )
            db.session.add(new_user)
            db.session.commit()
            print(f"New user created: {new_user}")
            login_user(new_user, remember=True)
            flash("Account created successfully!", category="success")
            return redirect(url_for("views.home"))
        except Exception as e:
            print(f"Error during signup: {e}")
            flash("An error occurred. Please try again.", category="error")
            return redirect(url_for("auth.sign_up"))
        
       
    return render_template("sign_up.html")




@auth.route('/option1_1')
@login_required
def option1_1():
    return render_template('/options/option 1/option1_1.html')

@auth.route('/option1_2')
@login_required
def option1_2():
    return render_template('/options/option 1/option1_2.html')

@auth.route('/option1_2_1')
@login_required
def option1_2_1():
    return render_template('/options/option 1/option1_2_1.html')

@auth.route('/option1_4_1')
@login_required
def option1_4_1():
    return render_template('/options/option 1/option1_4_1.html')

@auth.route('/option1_3')
@login_required
def option1_3():
    return render_template('/options/option 1/option1_3.html')

@auth.route('/option2_1')
@login_required
def option2_1():
    return render_template('/options/option 2/option2_1.html')

@auth.route('/option2_2')
@login_required
def option2_2():
    return render_template('/options/option 2/option2_2.html')

@auth.route('/option2_3')
@login_required
def option2_3():
    return render_template('/options/option 2/option2_3.html')

@auth.route('/option3_1')
@login_required
def option3_1():
    return render_template('/options/option 3/option3_1.html')

@auth.route('/option3_2')
@login_required
def option3_2():
    return render_template('/options/option 3/option3_2.html')

@auth.route('/option3_3')
@login_required
def option3_3():
    return render_template('/options/option 3/option3_3.html')

@auth.route('/option1_4')
@login_required
def option1_4():
    return render_template('/options/option 1/option1_4.html')

@auth.route('/option2_4')
@login_required
def option2_4():
    return render_template('/options/option 2/option2_4.html')

@auth.route('/option3_4')
@login_required
def option3_4():
    return render_template('/options/option 3/option3_4.html')

@auth.route('/option1_5')
@login_required
def option1_5():
    return render_template('/options/option 1/option1_5.html')

@auth.route('/option2_5')
@login_required
def option2_5():
    return render_template('/options/option 2/option2_5.html')

@auth.route('/option3_5')
@login_required
def option3_5():
    return render_template('/options/option 3/option3_5.html')
