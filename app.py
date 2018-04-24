from flask import Flask, render_template, url_for, redirect
import taskdb
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    tasks = taskdb.update_tasks()
    return render_template("index.html", taskmap = tasks)

if __name__ == '__main__':
    app.run()
