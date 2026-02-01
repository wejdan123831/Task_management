from fastapi import APIRouter, Query, Depends, HTTPException, Body
from typing import Annotated
from sqlalchemy.orm import Session
from schemas.models import TaskCreate
from database import models, database

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.get("/")
async def get_tasks(
    status: Annotated[str | None, Query(max_length=20)] = None,
    db: Session = Depends(database.get_db)
):
    query = db.query(models.Task)
    if status:
        query = query.filter(models.Task.status == status)
    tasks = query.all()
    return {"message": "List of tasks", "filter": status, "tasks": tasks}

@router.get("/all")
async def get_all_tasks(db: Session = Depends(database.get_db)):
    tasks = db.query(models.Task).all()
    return {"total_n": len(tasks), "tasks": tasks}

@router.post("/")
async def create_new_task(task: TaskCreate, db: Session = Depends(database.get_db)):
    # Check if user exists
    #user = db.query(models.User).filter(models.User.id == task.assign_user).first()
    #if not user:
     #   raise HTTPException(status_code=404, detail=f"Assigned User ID {task.assign_user} not found")
    
    # Create Task
    new_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority,
        owner_id=task.assign_user
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
            
    return {"message": "Task created successfully", "task": new_task}

@router.patch("/{task_id}/status")
async def update_task_status(task_id: int, status: str = Body(..., embed=True), db: Session = Depends(database.get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    valid_statuses = ["todo", "in progress", "completed"]
    if status not in valid_statuses:
        raise HTTPException(status_code=400, detail="Invalid status")
        
    task.status = status
    db.commit()
    db.refresh(task)
    return {"message": "Status updated successfully", "task": task}