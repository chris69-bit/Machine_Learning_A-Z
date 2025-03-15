from fastapi import FastAPI, Depends, status
import models
from database import engine, SessionLocal
from schemas import Blog
from sqlalchemy.orm import Session
# import uvicorn

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

@app.get("/blog")
def all(db: Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "Blog list"}

@app.get("/blog/{id}")
def page(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog

@app.get("/blog/{id}/comments")
def comments(id: int, limit=10):
    return {"data": "Blog list"}

    
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)