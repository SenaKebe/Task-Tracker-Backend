from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel, Field


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
