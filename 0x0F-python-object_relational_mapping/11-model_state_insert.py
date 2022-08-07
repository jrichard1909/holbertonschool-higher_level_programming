#!/usr/bin/python3
"""
Script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Base.metadata.create_all(engine)
    session = Session(bind=engine)
    session.add(State(name='Louisiana'))
    session.commit()
    result = session.query(State).filter(State.name == 'Louisiana').first()
    if result is not None:
        print(result.id)

    session.close()
