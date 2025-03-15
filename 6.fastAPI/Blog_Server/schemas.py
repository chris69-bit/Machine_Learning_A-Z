from pydantic import BaseModel
from typing import Optional

# Create a Blog
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]