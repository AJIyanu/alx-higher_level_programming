#!/usr/bin/python3

from sqlalchemy 
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask

Base = declarative_base()

class State(Base):
    """This needs to be documented and it is now"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name =  Column(String(128), nullable=False)
