# 1. initilise virtual environment (in cd kanban) python3 -m venv venv
# 2. flask --app flaskr run --debug

import os
from flask import Flask

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
        return 'Welcome to Kanban!' # format this + add button to Kanban
    
    @app.route('/kanban')
    def kanban():
        return 'Kanban Coming Soon!'

    # connects database
    from . import db
    db.init_app(app)
    
    # connects blueprint
    # from . import tasks
    # app.register_blueprint(tasks)
    # app.add_url_rule('/', endpoint='index')

    return app