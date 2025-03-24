from fastapi import FastAPI
from data import tasks

app = FastAPI()

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task):
    tasks.append(task)
    return f'task added'

@app.put("/tasks/{task_id}")
def update_task(task_id: int, name, status):
    for task in tasks:
        if task['id'] == task_id:
            task['name'] = name
            task['status'] = status
            return f'tasks updated'
    raise ValueError(f'task not found')


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return f'task removed'
    raise ValueError(f'task not found')

