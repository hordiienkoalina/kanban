from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from flaskr.models import Task, db

kanban = Blueprint('kanban', __name__)

@kanban.route('/board')
@login_required
def board():
    todo_tasks = Task.query.filter_by(status='ToDo', user_id=current_user.id).all()
    doing_tasks = Task.query.filter_by(status='Doing', user_id=current_user.id).all()
    done_tasks = Task.query.filter_by(status='Done', user_id=current_user.id).all()
    return render_template('board.html', title='Board - Kanban!', todo_tasks=todo_tasks, doing_tasks=doing_tasks, done_tasks=done_tasks)

@kanban.route('/add_task', methods=['POST'])
@login_required
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    status = request.form.get('status')
    task = Task(title=title, description=description, status=status, user_id=current_user.id)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('kanban.board'))

@kanban.route('/delete_task/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('kanban.board'))

@kanban.route('/update_task/<int:task_id>', methods=['POST'])
@login_required
def update_task(task_id):
    task = Task.query.get(task_id)
    task.title = request.form.get('title')
    task.description = request.form.get('description')
    task.status = request.form.get('status')
    db.session.commit()
    return redirect(url_for('kanban.board'))

@kanban.route('/move_task/<int:task_id>', methods=['POST'])
@login_required
def move_task(task_id):
    task = Task.query.get(task_id)
    task.status = request.form.get('status')
    db.session.commit()
    return redirect(url_for('kanban.board'))