from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks
tasks = []

# Load tasks from file
def load_tasks():
    global tasks
    try:
        with open("tasks.txt", "r") as f:
            tasks = [line.strip().split("|") for line in f.readlines()]
            tasks = [{"task": t[0], "completed": t[1] == "True"} for t in tasks]
    except FileNotFoundError:
        tasks = []

# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as f:
        for t in tasks:
            f.write(f"{t['task']}|{t['completed']}\n")

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("task")
    if task_name:
        tasks.append({"task": task_name, "completed": False})
        save_tasks()
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
        save_tasks()
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks()
    return redirect(url_for("index"))

if __name__ == "__main__":
    load_tasks()
    app.run(debug=True)
