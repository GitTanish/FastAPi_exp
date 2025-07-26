 # SQLAlchemy or ORM uses to be able to create the tables
# that we need in our MySqlDatabase

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String(50), unique=True)
    posts = relationship('Post', back_populates = 'creator')

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index = True)
    title = Column(String(50))
    content = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates="posts")