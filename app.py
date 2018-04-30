from flask import Flask, render_template, url_for, redirect, request
import taskdb
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    tasks = taskdb.update_tasks()
    return render_template("index.html", taskmap = tasks)

@app.route('/insert',methods=['POST'])
def insert():
    new = request.form['new']
    urgent = request.form.get('urgent')
    if urgent == "on":
        urgent = 1
    else:
        urgent = 0
    taskdb.insert_task(new, urgent)
    return redirect(url_for('index'))

@app.route('/delete/<task_id>')
def delete(task_id):
    taskdb.remove_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
