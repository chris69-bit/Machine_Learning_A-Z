from pydantic import BaseModel
from typing import Optional

# Create a Blog
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    
# Extend the Blog model
class BlogExtended(Blog):
    title: str
    body: str
    class Config:
        orm_mode = True
        
# Create a User
class User(BaseModel):
    username: str
    email:str
    password: str

class ShowUser(BaseModel):
    username: str
    email: str
    class Config:
        orm_mode = True