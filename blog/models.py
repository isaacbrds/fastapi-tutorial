from sqlalchemy import Column, Integer, String
from .database import Base

class Post(Base):
  __tablename__ = 'post'
  
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  description = Column(String)
