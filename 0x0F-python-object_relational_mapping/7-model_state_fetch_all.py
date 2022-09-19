#!/usr/bin/python3
"""
python script that contains the class
definition of a State and an instance
Base = declarative_base:
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()