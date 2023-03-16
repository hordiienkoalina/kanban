#  DB model

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flaskr import db, login_manager

# User model
# Inherits from UserMixin, which has properties for authentication
class User(UserMixin, db.Model):
    # User model atrributes
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    tasks = db.relationship('Task', backref='assignee', lazy='dynamic')

    # Representation of User as email string
    def __repr__(self):
        return f'<User {self.email}>'

    # Generates password hashinstead of using user input directly
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Checks stored password_hash against entered password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Task model
class Task(db.Model):
    # Task model atrributes
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Representation of Task as title string
    def __repr__(self):
        return f'<Task {self.title}>'

# Used to load users from the database based on their ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))