from flask import render_template, redirect, url_for, request
from .models import Task
from . import bp

@bp.route('/', methods=['GET'])
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@bp.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    task = Task(title=title, description=description)
    task.save()
    return redirect(url_for('tasks.index'))

@bp.route('/move_task/<int:task_id>/<string:state>', methods=['POST'])
def move_task(task_id, state):
    task = Task.query.get_or_404(task_id)
    task.state = state
    task.save()
    return redirect(url_for('tasks.index'))

@bp.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.delete()
    return redirect(url_for('tasks.index'))
