from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
from fastapi import HTTPException
from typing import List


app = FastAPI(title="Task Manager API")

from enum import Enum

class StatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
class TaskBase(BaseModel):
    title: str = Field(..., title="Title", example="Write blog post")
    description: Optional[str] = Field(default=None, title="Description", example="Write about FastAPI")
    status: StatusEnum = Field(..., title="Status", example="pending")
    priority: PriorityEnum = Field(..., title="Priority", example="high")



class Task(TaskBase):
    id: int

# In-memory "database"
tasks: List[Task] = []
next_id = 1

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskBase):
    global next_id
    new_task = Task(id=next_id, **task.dict())
    tasks.append(new_task)
    next_id += 1
    return new_task
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: TaskBase):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            tasks[i] = Task(id=task_id, **updated_task.dict())
            return tasks[i]
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            del tasks[i]
            return
    raise HTTPException(status_code=404, detail="Task not found")

