#!/usr/bin/python3
"""SQLALCHEMY"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

b = declarative_base()


class State(b):
    """State Class"""

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=True, primary_key=True)
    name = Column(String(128), nullable=False)
