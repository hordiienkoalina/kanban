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
export FLASK_APP=app.py
flask db init
flask db migrate -m "test"
flask db upgrade
```
## Testing
```
python3 -m unittest discover
```

## Sources
1. https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog
2. https://github.com/cleysondiego/simple-kanban-board/tree/master 

## Assignment Instructions
https://github.com/minerva-university/cs162/blob/1e6a861f165b8e0abef77fb3b4a885ceb25eda5a/assignments/web_application.md