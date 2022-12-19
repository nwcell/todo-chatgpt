from typing import List
from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from tortoise.exceptions import DoesNotExist

app = FastAPI()

# Define your database models
class Task(Base):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    completed = fields.BooleanField(default=False)

# Initialize Tortoise-ORM and register the models
register_tortoise(app, db_url="sqlite://db.sqlite3", modules={"models": ["app.models"]}, generate_schemas=True)

# Define your API routes

@app.post("/tasks")
async def create_task(task: Task, db=Depends(get_db)):
    await task.save()
    return task

@app.get("/tasks")
async def read_tasks(skip: int = 0, limit: int = 100, db=Depends(get_db)):
    tasks = await Task.all().offset(skip).limit(limit).prefetch_related("tags").execute()
    return tasks

@app.get("/tasks/{task_id}")
async def read_task(task_id: int, db=Depends(get_db)):
    try:
        task = await Task.get(id=task_id)
    except DoesNotExist:
        raise HTTPNotFoundError("Task not found")
    return task

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task, db=Depends(get_db)):
    try:
        existing_task = await Task.get(id=task_id)
    except DoesNotExist:
        raise HTTPNotFoundError("Task not found")
    existing_task.title = task.title
    existing_task.description = task.description
    existing_task.completed = task.completed
    await existing_task.save()
    return existing_task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db=Depends(get_db)):
    try:
        task = await Task.get(id=task_id)
    except DoesNotExist:
        raise HTTPNotFoundError("Task not found")
    await task.delete()
    return {"message": "Task deleted"}

# Define a function to return a database session for dependency injection
async def get_db(request):
    return request.app.state.db
