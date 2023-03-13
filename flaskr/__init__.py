import os
from flask import Flask, render_template, url_for, flash, redirect
# from flask_sqlalchemy import SQLAlchemy
# from .forms import RegistrationForm, LoginForm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from instance.config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    from routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from routes.kanban import kanban as kanban_blueprint
    app.register_blueprint(kanban_blueprint)

    return app


from flaskr import models


# def create_app(test_config=None):
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
#     )
    
    
#     # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#     # db = SQLAlchemy(app)
    
#     # class Task(db.Model):
#     #     id = db.Column(db.Integer, primary_key=True)
#     #     title = db.Column(db.String(100), nullable=False)
#     #     description = db.Column(db.String(200))
#     #     status = db.Column(db.String(20), default='ToDo')
#     #     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     #     user = db.relationship('User', backref=db.backref('tasks', lazy=True))
    
#     if test_config is None:
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         app.config.from_mapping(test_config)
    
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass
    
#     # move this to /routes
#     @app.route('/')
#     @app.route('/home')
#     def home():
#         return render_template('kanban.html', title='Board - Kanban!')
    
#     @app.route('/register', methods=['GET', 'POST'])
#     def register():
#         form = RegistrationForm()
#         if form.validate_on_submit():
#             flash(f'Account created for {form.username.data}!', 'success')
#             return redirect(url_for('home'))
#         return render_template('register.html', title='Register - Kanban!', form=form)
    
#     @app.route('/login', methods=['GET', 'POST'])
#     def login():
#         form = LoginForm()
#         if form.validate_on_submit():
#             if form.email.data == 'admin@kanban.com' and form.password.data == 'password':
#                 flash('You have been logged in!', 'success')
#                 return redirect(url_for('home'))
#             else:
#                 flash('Login Unsuccessful. Please check username and password', 'danger')
#         return render_template('login.html', title='Log In - Kanban!', form=form)

#     return app