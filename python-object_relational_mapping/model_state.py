#!/usr/bin/python3
"""SQLALCHEMY"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State Class"""

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=True, primary_key=True)
    name = Column(String(128), nullable=False)
