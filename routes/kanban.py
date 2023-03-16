# Kanban Blueprint
# NEEDS FIXING

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from flaskr.models import Task, db
from flaskr.forms import AddTaskForm
from flask_wtf.csrf import generate_csrf

kanban = Blueprint('kanban', __name__)

@kanban.route('/board', methods=['GET', 'POST'])
@login_required
def board():
    form = AddTaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, status=form.status.data, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully.', 'success')
        return redirect(url_for('kanban.board'))

    todo_tasks = Task.query.filter_by(user_id=current_user.id, status='ToDo').all()
    doing_tasks = Task.query.filter_by(user_id=current_user.id, status='Doing').all()
    done_tasks = Task.query.filter_by(user_id=current_user.id, status='Done').all()

    return render_template('kanban.html', todo_tasks=todo_tasks, doing_tasks=doing_tasks, done_tasks=done_tasks, form=form, csrf_token=form.csrf_token._value())

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