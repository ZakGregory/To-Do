from flask import render_template, redirect, request, url_for
from application import app, db
from application.models import Tasks
from application.forms import InputForm
from sqlalchemy import asc, desc

@app.route('/')
@app.route('/home')
@app.route('/home/<method>')
def home(method=""):
    if method=="O-N":
        all_tasks=Tasks.query.filter().order_by(Tasks.id)
    elif method=="N-O":
        all_tasks=Tasks.query.filter().order_by(desc(Tasks.id))
    elif method=="CF":
        all_tasks=Tasks.query.filter().order_by(desc(Tasks.complete))
    elif method=="NCF":
        all_tasks=Tasks.query.filter().order_by(Tasks.complete)
    else:
        all_tasks=Tasks.query.all()
    return render_template('home.html', all_tasks=all_tasks)

@app.route('/add', methods=['GET','POST'])
def add():
    form = InputForm()

    if form.validate_on_submit():
        new_task = Tasks(name=form.new_task.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/complete/<taskid>')
def complete(taskid):
    task_to_update = Tasks.query.get(taskid)
    task_to_update.complete = True
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/incomplete/<taskid>')
def incomplete(taskid):
    task_to_update = Tasks.query.get(taskid)
    task_to_update.complete = False
    db.session.commit()
    return redirect(url_for('home'))
 
@app.route('/update/<taskid>', methods=['GET','POST'])
def update(taskid):
    form = InputForm()
    task_to_update = Tasks.query.get(taskid)
    
    if form.validate_on_submit():
        task_to_update.name = form.new_task.data        
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)
 

@app.route('/delete/<taskid>')
def delete(taskid):
    task_to_delete = Tasks.query.get(taskid)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
