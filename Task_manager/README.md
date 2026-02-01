# TeamSync: Professional Task Management System

TeamSync is a high-performance, minimalist task manager designed for collaborative efficiency. Built with **FastAPI**, it provides a streamlined experience for tracking objectives and monitoring team workload with a premium, high-contrast visual design.

## 🎨 Visual Identity: Modern Premium White
The application features a **Strict Minimalist White Theme** optimized for focus and clarity:
- **Typography:** Uses the modern 'Inter' sans-serif font for maximum legibility.
- **Aesthetics:** Soft shadows (`box-shadow: 0 10px 30px rgba(0,0,0,0.05)`) and `24px` rounded corners.
- **Micro-Interactions:** Frosted glass navigation dock with smooth hover effects.

## ✨ Key Features
- **Modern Dashboard:** A clean, bento-style interface for at-a-glance project monitoring.
- **Team Workload:** Real-time visual task distribution. Monitor active tasks for team members like **wejdan** and **Adam**.
- **Interactive Navigation:** A fixed floating dock for rapid transitions between Tasks, Team, and Profile views.
- **User Profiles:** Personalized profile pages with integrated status updates.
- **Strict Security:** Owner-only task update logic ensures data integrity.

## 🛠️ Tech Stack
- **Backend:** Python 3.10+ / FastAPI
- **Frontend:** Jinja2 Templates, Bootstrap 5.3, Modern Vanilla CSS3
- **Database:** SQLAlchemy with SQLite (local storage)
- **Icons & Animation:** Bootstrap Icons & Animate.css

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Task_manager
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Launch the development server using uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   *Last updated: 2026-01-30*

## 📂 Project Structure
- **`routers/`**: Contains the core logic for API endpoints (`tasks.py`, `users.py`).
- **`schemas/`**: Pydantic models for request validation and data serialization.
- **`database/`**: Database configuration and SQLAlchemy models.
- **`templates/`**: Professional Jinja2 HTML templates styled with our custom Minimalist White Theme.
- **`main.py`**: The central application entry point where routers and templates are initialized.

---
*Built for teams that value speed and simplicity.*
