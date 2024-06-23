#!/usr/bin/python3
"""
Python file that contains the class definition of a State and an instance
"""
from sqlalchemy.ext.declarative import declerative_base
from sqlalchemy import Column, String, integer

Base = declerative_base()

class State(Base):
     """
    State class that inherits from Base

    Attributes:
        id: Id state
        name: Name of state
    """
     __tablename__ = "states"
     id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
     name = Column(String(128), nullable=False)
