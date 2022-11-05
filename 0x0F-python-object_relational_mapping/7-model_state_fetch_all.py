#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    connection = engine.connect()
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    results = session.query(State).all()

    count = 1
    for states in results:
        print("{}: {}".format(count, states.name))
        count = count + 1
