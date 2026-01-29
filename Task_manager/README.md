# Task Management System

This project is a Task Management System built using **FastAPI**. It is designed to demonstrate efficient task management with a focus on modular code structure and robust data validation.

## Key Features

- **FastAPI Framework**: High-performance, easy-to-learn framework for building APIs with Python 3.7+.
- **Router Modularization**: The application is structured using `APIRouter` to keep code organized and maintainable.
  - User operations are handled in `routers/users.py`.
  - Task operations are handled in `routers/tasks.py`.
- **Data Validation**: Uses **Pydantic** models (located in `schemas/models.py`) to ensure that input data is valid and consistent.

## Project Structure

```
Task_manager/
├── main.py              # Entry point of the application
├── routers/             # API routes
│   ├── tasks.py         # Task-related routes
│   └── users.py         # User-related routes
└── schemas/             # Pydantic models
    └── models.py        # Data schemas for validation
```

## How to Run

1.  Make sure you have Python installed.
2.  Install the required dependencies (if not already installed):
    ```bash
    pip install fastapi uvicorn
    ```
3.  Run the server using `uvicorn`:
    ```bash
    uvicorn main:app --reload
    ```
4.  Open your browser and navigate to `http://127.0.0.1:8000/docs` to see the interactive API documentation.
