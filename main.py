from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index(limit=0, sort: Optional[str] = None):
  if limit:
    return {'data': f'{limit} posts from db' }
  else:
    return {'data': f'all posts from db'}


@app.get('/blog/unpublished')  
def unpublished():
  return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id):
  return {'data': id }

class Blog(BaseModel):
  title: str
  description: str
  published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
  return {'data': "Post is created"}