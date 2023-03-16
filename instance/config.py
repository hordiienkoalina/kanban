import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret key to sign cookies, environment variable 'SECRET_KEY' or default to 'dev'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    
    # Database configuration, environment variable 'DATABASE_URL' or default to SQLite local database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # Disable tracking of modifications for SQLAlchemy, to improve performance and save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False