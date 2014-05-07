# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# system dependencies: libmysqlclient-dev + python-dev
# then install this mysql driver for python: pip install mysql-python

# this will be called by settings.py to initialize the session class only once
def init_session(conf):
    engine = create_engine("mysql://%s:%s@%s/%s?%s" % (
        conf['LOGIN'],
        conf['PASSWORD'],
        conf['HOST'],
        conf['DATABASE'],
        conf['OPTIONS'],
    ), echo = True)
    return scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

class Album(Base):
    __tablename__ = 'album'

    id = Column(Integer, primary_key = True)
    artist = Column(String(100))
    title = Column(String(100))
