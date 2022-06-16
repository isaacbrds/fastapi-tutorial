from fastapi import FastAPI, Depends
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.post('/blog')
def create(request: schemas.Post, db: Session = Depends(get_db)): 
  new_post = models.Post( title=request.title, description=request.description)
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post
