# -*- coding: utf-8 -*-

from django.conf import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session

# system dependencies: libmysqlclient-dev + python-dev
# then install this mysql driver for python: pip install mysql-python

# TODO: create and close db session in a middleware

engine = create_engine("mysql://%s:%s@%s/%s?%s" % (
    settings.DATABASE['LOGIN'],
    settings.DATABASE['PASSWORD'],
    settings.DATABASE['HOST'],
    settings.DATABASE['DATABASE'],
    settings.DATABASE['OPTIONS'],
), echo = True)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

Base = declarative_base()

class Album(Base):
    __tablename__ = 'album'

    id = Column(Integer, primary_key = True)
    artist = Column(String(100))
    title = Column(String(100))
