from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from routers import users, tasks
from database import models, database

app = FastAPI(title="Task Management System")

# Create Database Tables
models.Base.metadata.create_all(bind=database.engine)

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Include the routers
# Include the routers
app.include_router(users.router)
app.include_router(tasks.router)

from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import http_exception_handler

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return templates.TemplateResponse("error.html", {"request": request, "error_detail": str(exc)}, status_code=500)

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/profile", response_class=HTMLResponse)
async def profile_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})

@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request, db: Session = Depends(database.get_db)):
    # Fetch users from DB
    users_data = db.query(models.User).all()
    return templates.TemplateResponse("index.html", {"request": request, "users": users_data})

@app.get("/tasks-page", response_class=HTMLResponse)
async def read_tasks(request: Request, db: Session = Depends(database.get_db)):
    tasks_data = db.query(models.Task).all()
    users_data = db.query(models.User).all()
    return templates.TemplateResponse("tasks.html", {"request": request, "tasks": tasks_data, "users": users_data})

@app.get("/assignments-page", response_class=HTMLResponse)
async def read_assignments(request: Request, db: Session = Depends(database.get_db)):
    # Fetch users with eager loaded tasks (SQLAlchemy handles relationship access in template)
    users_data = db.query(models.User).all()
    # Format for template expects assignments list
    assignments = []
    for u in users_data:
        assignments.append({
            "user_id": u.id,
            "username": u.username,
            "tasks": [t.title for t in u.tasks]
        })
    return templates.TemplateResponse("assignments.html", {"request": request, "assignments": assignments})

@app.get("/api-root")
async def root():
    return {"message": "Welcome to the Task API"}