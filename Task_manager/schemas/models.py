
from pydantic import BaseModel, Field, field_validator
from typing import List, Literal, Annotated, Optional


class Profile(BaseModel):
    bio: Optional[str] = Field(None, max_length=150)
    website: Optional[str] = None
    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    role: Literal["admin", "manager", "team member"] 
    profile: Profile 
    class Config:
        from_attributes = True

# i need 3 pages 
# page 1  all user
#page 2 all task 
# page 3 each user with task 
class TaskCreate(BaseModel):
    title: str
    description: str
    status: Literal["todo", "in progress", "completed"] 
    priority: Annotated[int, Field(ge=1, le=5)] 
    assign_user : int
    class Config:
        from_attributes = True

    @field_validator('title')
    @classmethod
    def title_must_be_capitalized(cls, v: str) -> str:
        if not v[0].isupper():
            raise ValueError('Title must start with a capital letter')
        return v