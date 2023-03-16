# Kanban

## Overview
~ TBD ~
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