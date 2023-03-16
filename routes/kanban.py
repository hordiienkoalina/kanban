# Kanban Blueprint
# NEEDS FIXING

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from flaskr.models import Task, db
from flaskr.forms import NewTaskForm

kanban = Blueprint('kanban', __name__)

@kanban.route('/board')
@login_required
def board():
    # Get all tasks of the user filtered by status
    todo_tasks = Task.query.filter_by(status='ToDo', user_id=current_user.id).all()
    doing_tasks = Task.query.filter_by(status='Doing', user_id=current_user.id).all()
    done_tasks = Task.query.filter_by(status='Done', user_id=current_user.id).all()
    # Render the kanban board template with the tasks
    return render_template('kanban.html', title='Board - Kanban!', todo_tasks=todo_tasks, doing_tasks=doing_tasks, done_tasks=done_tasks)

@kanban.route('/add_task', methods=['POST', 'GET'])
@login_required
def add_task():
    form = NewTaskForm()
    if form.validate_on_submit():
        # Get the form data for title
        title = request.form['title']
        # Create a new Task object with the form data
        task = Task(title=title, status="todo")
        # Add the task to the database
        db.session.add(task)
        db.session.commit()
        # Flash a success message to be displayed on the next request
        flash(f'Task "{title}" created!', 'success')
        # Redirect to the kanban board page
    return redirect(url_for('kanban'))
    
@kanban.route('/delete_task/<int:task_id>',  methods=['POST', 'GET'])
@login_required
def delete_task(task_id):
    # Get the task with the given id from the database
    task = Task.query.get(task_id)
    # Remove the task from the database
    db.session.delete(task)
    db.session.commit()
    # Redirect to the kanban board page
    return redirect(url_for('kanban.board'))

@kanban.route('/update_task/<int:task_id>',  methods=['POST', 'GET'])
@login_required
def update_task(task_id):
    # Get the task with the given id from the database
    task = Task.query.get(task_id)
    # Update the task with the form data
    task.title = request.form.get('title')
    task.status = request.form.get('status')
    # Commit the changes to the database
    db.session.commit()
    # Redirect to the kanban board page
    return redirect(url_for('kanban.board'))

@kanban.route('/move_task/<int:task_id>',  methods=['POST', 'GET'])
@login_required
def move_task(task_id):
    # Get the task with the given id from the database
    task = Task.query.get(task_id)
    # Update the task status with the new status from the form data
    task.status = request.form.get('status')
    # Commit the changes to the database
    db.session.commit()
    # Redirect to the kanban board page
    return redirect(url_for('kanban.board'))