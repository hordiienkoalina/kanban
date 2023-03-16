# Kanban

## Kanban App
This Kanban app is a simple, yet powerful task management tool designed to help you organize and prioritize your tasks effectively. It is built using Python, Flask, and SQLite, providing a lightweight and easy-to-use solution for managing tasks in a visual way.

### Features
1. **User authentication**: The app allows users to sign up, log in, and log out, ensuring that tasks are only accessible to their respective users.
2. **Task managemen**t: Users can create, edit, and delete tasks with customizable titles and descriptions.
3. **Responsive design**: The app is built using Flask-Bootstrap, making it responsive and mobile-friendly.
### Tech Stack
1. **Backend**: Python 3, Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Login
2. **Frontend**: HTML, CSS, JavaScript, Bootstrap
3. **Database**: SQLite
4. **Testing**: Python's unittest module

To get started with this Kanban app, simply follow the installation instructions provided in the repository. Enjoy organizing your tasks and improving your productivity with this intuitive and user-friendly tool!
## Install
macOS:
```
python3 -m venv test-venv
source test-venv/bin/activate
pip3 install -r requirements.txt
python3 run.py
```
Windows:
```
python3 -m venv test-venv
test-venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3 run.py
```
## Initialise DB
```
export FLASK_APP="flaskr:create_app()" 
flask db init
flask db migrate -m "test"
flask db upgrade
```
## Testing
```
python3 -m unittest discover
```
and/or
```
coverage run run_tests.py
coverage report
coverage html
```

## Sources
1. https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog