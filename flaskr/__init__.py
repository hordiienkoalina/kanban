# 1. initilise virtual environment (in cd kanban) python3 -m venv venv
# 2. flask --app flaskr run --debug

import os
from flask import Flask, render_template, url_for, flash, redirect
from .forms import RegistrationForm, LoginForm

def create_app(test_config=None):
    # creates and configures the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    
    if test_config is None:
        # loads the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # loads the test config if passed in
        app.config.from_mapping(test_config)
    
    # ensures the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # kanban as homepage
    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('kanban.html', title='Board - Kanban!')
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
        return render_template('register.html', title='Register - Kanban!', form=form)
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            if form.email.data == 'admin@kanban.com' and form.password.data == 'password':
                flash('You have been logged in!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
        return render_template('login.html', title='Log In - Kanban!', form=form)

    # connects database
    from . import db
    db.init_app(app)
    
    # connects blueprint
    # from . import tasks
    # app.register_blueprint(tasks)
    # app.add_url_rule('/', endpoint='index')

    return app