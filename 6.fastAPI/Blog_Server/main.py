from fastapi import FastAPI, Depends
import models
from database import engine, SessionLocal
from schemas import Blog
from sqlalchemy.orm import Session
# import uvicorn

models.Base.metadata.create_all(bind=engine)

# Decorator
app = FastAPI()

# Read Operations
@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/blog")
def show(limit=10, published: bool = True, sort: str = None):
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from the db"}

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "Blog list"}

@app.get("/blog/{id}")
def page(id: int):
    return {"data": "Blog list"}

@app.get("/blog/{id}/comments")
def comments(id: int, limit=10):
    return {"data": "Blog list"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    
@app.post("/blog")
def create_blog(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog
    
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)