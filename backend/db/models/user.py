from db.base_class import Base
from sqlalchemy import Column, Boolean,Integer, String
from sqlalchemy.orm import relationship

from .blog import Blog

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email= Column(String, nullable=False, unique=True, index=True)
    password=Column(String, nullable=False)
    is_active=Column(Boolean, default=True)
    blogs=relationship("Blog",back_populates="author")
    