from fastapi import FastAPI, Depends, status, Response, HTTPException
import models
from database import engine, SessionLocal
from schemas import Blog, BlogExtended, User, ShowUser
from sqlalchemy.orm import Session
from typing import List
from hashing import Hash
#from passlib.context import CryptContext
#import uvicorn

models.Base.metadata.create_all(bind=engine)

# Decorator
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    
@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog


# Read Operations

@app.get("/blog") #response_model=List[BlogExtended]
def all(db: Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog

# @app.get("/blog/unpublished")
# def unpublished():
#     return {"data": "Blog list"}

@app.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=BlogExtended)
def page(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": "Blog with the given id not found"}
    else:
        return blog

# @app.get("/blog/{id}/comments")
# def comments(id: int, limit=10):
#     return {"data": "Blog list"}

#Update Items
@app.put("/blog/{id}", status_code = status.HTTP_202_ACCEPTED)
def update(id: int, request: Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.update(request)
    db.commit()
    return{"details": "Blog updated successfully"}

# Delete Items
@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"details" : "Blog deleted successfully"}


   
#Adding a user to the database


@app.post("/user", status_code = status.HTTP_201_CREATED, response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    new_user = models.User(username=request.username, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

    
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)