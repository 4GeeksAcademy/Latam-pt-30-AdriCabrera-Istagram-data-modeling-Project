import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    # Relacion con seguidor
    follower = relationship('Follower', back_populates='user')
    # Relacion con comentarios
    comment = relationship('Comment', back_populates='user')
    # Relacion con post
    post = relationship('Post', back_populates='user')

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    # Relacion con usuario
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='follower')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment = Column(String(250))
    # Relacion con usuario
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='comment')
    # Relacion con Post
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post', back_populates='post')

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    # Relacion con usuario
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='like')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    # Relacion con usuario
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='post')
    # Relacion con comentario
    comment_id = Column(Integer, ForeignKey('comment.id'))
    comment = relationship('Comment', back_populates='post')
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
