#!/usr/bin/python3
"""
Script that prints all City objects from
the database hbtn_0e_14_usa
"""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = Session(bind=engine)
    result = session.query(State.name, City.id, City.name).join(State).all()
    for state in result:
        print("{}: ({}) {}".format(state[0], state[1], state[2]))
