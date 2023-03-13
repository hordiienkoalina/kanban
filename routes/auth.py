# User Auth Blueprint

from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from flaskr.models import User, Task
from flaskr import db
from flaskr.forms import SignupForm, LoginForm

# Create new blueprint named 'auth'
auth = Blueprint('auth', __name__)

# Route to render the homepage
@auth.route('/')
@auth.route('/home')
def home():
    return render_template('kanban.html')

@auth.route('/login')
def login():
    form = LoginForm()
    # If form submitted and validated 
    if form.validate_on_submit():
        # Redirect to Kanban
        return redirect(url_for('auth.home'))
    # Else, rander Login page
    return render_template('login.html', form=form)

@auth.route('/login', methods=['POST', 'GET'])
def login_post():
    with current_app.app_context():
        # Get the email, password, and remember me status from the login form
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        
        # Get the user with the submitted email address from the database
        user = User.query.filter_by(email=email).first()

        # If user not found or password is incorrect
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))

        # If Login successful, redirect to Kanban and set RememberMe status
        login_user(user, remember=remember)
        return redirect(url_for('auth.home'))

@auth.route('/signup')
def signup():
    form = SignupForm()
    # If form submitted and validated 
    if form.validate_on_submit():
        # Redirect to Kanban
        return redirect(url_for('auth.home'))
    # Else, rander Signup page
    return render_template('signup.html', form=form)

@auth.route('/signup', methods=['POST', 'GET'])
def signup_post():
    with current_app.app_context():
        # Get the email, password, and remember me status from the login form
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        # Get the user with the submitted email address from the database
        user = User.query.filter_by(email=email).first()

        # If email already exists
        if user:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        # If Signup successful, add user to DB and commit
        new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()

        # Redirect to Login
        return redirect(url_for('auth.login'))

# Logout route
@auth.route('/logout')
# Restricts access only to authenticated users
@login_required
def logout():
    # Logs out the user using Flask-Login's logout_user() function
    logout_user()
    # Redirects user to the login page
    return redirect(url_for('auth.login'))