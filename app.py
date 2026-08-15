from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

todos = []
next_id = 1


@app.route('/', methods=['GET', 'POST'])
def home():

    global next_id

    if request.method == 'POST':

        title = request.form['title']
        desc = request.form['desc']

        todo = {
            "sno": next_id,
            "title": title,
            "desc": desc,
            "date_created": datetime.now(),
            "status": "Pending"
        }
        todos.append(todo)
        next_id += 1

    return render_template("index.html", allTodo=todos)



@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = None
    for task in todos:
        if task["sno"] == sno:
            todo = task
            break

    if todo is None:
        return "Task Not Found"

    if request.method == "POST":

        todo["title"] = request.form["title"]
        todo["desc"] = request.form["desc"]

        return redirect("/")

    return render_template("update.html", todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    for task in todos:
        if task["sno"] == sno:
            todos.remove(task)
            break
    return redirect("/")

@app.route('/mark/<int:sno>')
def mark_completed(sno):
    for task in todos:
        if task["sno"] == sno:
            task["status"] = "Completed"
            break
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)