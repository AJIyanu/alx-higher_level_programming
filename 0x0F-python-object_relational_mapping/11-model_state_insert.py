#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)

    connection = engine.connect()
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    Louisiana = State()
    Louisiana.name = "Louisiana"
    session.add(Louisiana)
    session.commit()
    results = session.query(State).filter(State.name.like("Arizona"))
    print(results)
    session.close()
