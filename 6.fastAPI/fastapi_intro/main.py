from fastapi import FastAPI

app = FastAPI()

@app.get("/blog?limit=10&published=true")
def index():
    return {'data': 'blog list'}

@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get("/blog/{id}")
def about_page(id: int):
    return {'data': id }

# @app.get("/blog/{id}/comments")
# def comments(id):
#     return {'data': {'1', '2'}}


