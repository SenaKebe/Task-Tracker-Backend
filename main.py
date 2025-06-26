from fastapi import FastAPI
from enum import Enum

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
