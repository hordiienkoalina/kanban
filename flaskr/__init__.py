from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from instance.config import Config

# Initialize the extensions
db = SQLAlchemy()  # Database extension
migrate = Migrate()  # Database migration extension
login_manager = LoginManager()  # User authentication extension
login_manager.login_view = 'auth.login'  # Set the login view for unauthorized access
bootstrap = Bootstrap()  # Front-end framework extension

def create_app():
    # Create the Flask application instance
    app = Flask(__name__)
    # Load configuration from Config class
    app.config.from_object(Config)

    # Initialize the extensions with the app instance
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    # Register the blueprints for different routes
    from flaskr.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from flaskr.routes.kanban import kanban as kanban_blueprint
    app.register_blueprint(kanban_blueprint)

    # Return the app instance
    return app