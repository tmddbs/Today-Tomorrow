from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from .models import Task
from . import db
import random


views = Blueprint('views', __name__)
quotes = [
    "\"가장 바쁜 사람이 가장 많은 시간을 갖는다\"",
    "\"미래를 예측하는 최선의 방법은 미래를 창조하는 것이다\"",
    "\"시간과 정성을 들이지 않고 얻을 수 있는 결실은 없다\"",
    "\"승자는 시간을 관리하며 살고 패자는 시간에 끌려 산다\"",
    "\"당신은 지체할 수도 있지만 시간은 그러지 않을 것이다\"",
    "\"시간은 우리를 변화시키지 않는다. 시간은 단지 우리를 펼쳐 보일 뿐이다\"",
    "\"지붕은 햇빛이 밝을 때 수리해야 한다\"",
    "\"오늘 회피한다고 내일의 책임에서 벗어날 수는 없다\"",
    "\"낭비한 시간에 대한 후회는 더 큰 시간 낭비이다\"",
    "\"10분 뒤와 10년 후를 동시에 생각하라\"",
    
]




@views.route('/task-create', methods=['GET', 'POST'])
@login_required
def task_form():

    if request.method == "POST":
        title = request.form.get('title')
        description = request.form.get('description')
        complete = request.form.get('complete')

        if complete:
            complete = True

        new_task = Task(title=title, description=description, complete=complete, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash("Task created!", category='success')
        return redirect(url_for('views.task_list'))

    return render_template("task_form.html", user=current_user)



    return render_template("task_form2.html", user=current_user)

@views.route('/task-delete/<int:id>', methods=['GET', 'POST'])
@login_required
def task_delete(id):
    task = Task.query.filter_by(id=id).first()
    if request.method == "POST":
        db.session.delete(task)
        db.session.commit()
        flash("Task Deleted!", category='success')
        return redirect(url_for("views.task_list"))

    return render_template("task_confirm_delete.html", task=task)


@views.route('/task-update/<int:id>', methods=['GET', 'POST'])
@login_required
def task_update(id):
    task = Task.query.filter_by(id=id).first()
    if request.method == "POST":
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        complete = request.form.get('complete')

        if complete:
            complete = True
        else:
            complete = False

        task.complete = complete
        db.session.commit()
        flash("Task Updated!", category='success')
        return redirect(url_for("views.task_list"))

    return render_template("task_update.html", task=task)


@views.route('/task_list', methods=['GET', 'POST'])
@login_required
def task_list():
    count = Task.query.filter_by(user_id=current_user.id, complete=False).count()
    plural = True if count > 1 else False
    tasks = current_user.tasks
    search_input = ''
    random_quote = random.choice(quotes)

    if request.method == "POST":
        search = request.form.get('search-area')
        search_input = search
        result = Task.query.filter(Task.title.like(f'%{search}%'), Task.user_id == current_user.id).all()
        tasks = result
        
    return render_template("task_list.html", user=current_user, plural=plural, count=count, tasks=tasks, random_quote=random_quote, search_input=search_input)

@views.route('/task_list1', methods=['GET', 'POST'])
@login_required
def task_list1():
    count = Task.query.filter_by(user_id=current_user.id, complete=False).count()
    plural = True if count > 1 else False
    tasks = current_user.tasks
    search_input = ''
    random_quote = random.choice(quotes)

    if request.method == "POST":
        search = request.form.get('search-area')
        search_input = search
        result = Task.query.filter(Task.title.like(f'%{search}%'), Task.user_id == current_user.id).all()
        tasks = result
        
    return render_template("task_list1.html", user=current_user, plural=plural, count=count, tasks=tasks, random_quote=random_quote, search_input=search_input)
@views.route('/task_list2', methods=['GET', 'POST'])
@login_required
def task_list2():
    count = Task.query.filter_by(user_id=current_user.id, complete=False).count()
    plural = True if count > 1 else False
    tasks = current_user.tasks
    search_input = ''
    random_quote = random.choice(quotes)

    if request.method == "POST":
        search = request.form.get('search-area')
        search_input = search
        result = Task.query.filter(Task.title.like(f'%{search}%'), Task.user_id == current_user.id).all()
        tasks = result
        
    return render_template("task_list2.html", user=current_user, plural=plural, count=count, tasks=tasks, random_quote=random_quote, search_input=search_input)