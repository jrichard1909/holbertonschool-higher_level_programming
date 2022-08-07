#!/usr/bin/python3
"""
Script that prints the first State object
from the database hbtn_0e_6_usa
"""
from os import stat
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
    statement = select(State)
    result = session.query(State).first()
    if result is not None:
        print("{}: {}".format(result.id, result.name))
    else:
        print('Nothing\n')
