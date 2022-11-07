#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)

    connection = engine.connect()
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    California = State()
    newcity = City()
    newcity.name = "San Francisco"
    newcity.state = California
    session.add(California, newcity)
    session.commit()
    results = session.query(State).all()
    for state in results:
        if state.name == "Louisiana":
            print(state.id)
    session.close()
