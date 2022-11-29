from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime


app = FastAPI()


posts = []


# Post model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime =  datetime.now()
    published_at: Optional[datetime] 
    published: Optional[bool] = False


@app.get("/")
def read_root():
    return {"welcome": "Welcome to my REST API"}


@app.get("/posts")
def get_posts():
    return posts


@app.post("/posts")
def save_post(post):
    print(post)
    return "I get it"