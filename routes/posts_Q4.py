from pydantic import BaseModel
from datetime import datetime
from fastapi import status
from typing import List

class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

posts_db: List[Post] = []

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(new_posts: List[Post]):
    posts_db.extend(new_posts)
    return posts_db