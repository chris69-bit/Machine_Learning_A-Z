from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

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


# Create a Blog
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    
@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"Blog is created with title as {request.title}"}
    
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)