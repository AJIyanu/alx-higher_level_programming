#!/usr/bin/python3
"""
python script that contains the class
definition of a State and an instance
Base = declarative_base:
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State

class City(Base):
    """A City clas that links to MySql table ciy"""

    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(length=128), nullable=False)
    states_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship(State)
