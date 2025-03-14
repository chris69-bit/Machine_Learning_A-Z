from fastapi import FastAPI
from pydantic import BaseModel

# Decorator
app = FastAPI()

# Read Operations
@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/blog")
def show(limit, published: bool):
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
def comments():
    return {"data": "Blog list"}


# Create a Blog
class Blog(BaseModel):
    title: str
    body: str
    
@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"Blog is created with title as {request.title}"}
    
