from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_
from schemas.models import UserCreate
from database import models, database
from pydantic import BaseModel
import hashlib

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Helper for Hashing
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

class LoginRequest(BaseModel):
    username: str # Can be username OR email from the frontend
    password: str

@router.get("/all")
async def get_all_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return {"total_n": len(users), "users": users}

@router.post("/")
async def register_user(user: UserCreate, db: Session = Depends(database.get_db)):
    # Check for existing user or email
    existing_user = db.query(models.User).filter(
        or_(
            models.User.username == user.username,
            models.User.email == user.email
        )
    ).first()
    
    if existing_user:
        if existing_user.username == user.username:
            raise HTTPException(status_code=400, detail="Username already exists")
        if existing_user.email == user.email:
             raise HTTPException(status_code=400, detail="Email already exists")

    # Create User with Hashed Password
    new_user = models.User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )
    db.add(new_user)
    db.commit() 
    
    # Create Profile
    if user.profile:
        new_profile = models.Profile(
            bio=user.profile.bio,
            website=user.profile.website,
            owner_id=new_user.id
        )
        db.add(new_profile)
        db.commit()

    db.refresh(new_user)
    
    return {"message": "User registered successfully", "user": new_user}

@router.post("/login")
async def login(login_data: LoginRequest, db: Session = Depends(database.get_db)):
    # Check for username OR email match
    user = db.query(models.User).filter(
        or_(
            models.User.username == login_data.username,
            models.User.email == login_data.username # The 'username' field in request carries the input string
        )
    ).first()
    
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username/email or password")
    
    # Verify Password
    if user.password != hash_password(login_data.password):
        raise HTTPException(status_code=400, detail="Invalid username/email or password")
        
    return {
        "message": "Login successful",
        "user_id": user.id,
        "username": user.username,
        "role": user.role
    }

# For assignments page (users with tasks)
@router.get("/with-tasks")
async def users_with_tasks(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    result = []
    for u in users:
        result.append({
            "user_id": u.id,
            "username": u.username,
            "tasks": [t.title for t in u.tasks]
        })
    return {"users": result}

@router.get("/{username}")
async def get_user_profile(username: str, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": user.username, "info": "User profile data", "profile": user.profile}
