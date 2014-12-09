from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()

def db_connect():
	return create_engine(URL(**settings.DATABASE))

def create_deals_table(engine):
	DeclarativeBase.metadata.create_all(engine)

class Deals(DeclarativeBase):

	__tablename__ = "deals"

	id = Column(Integer, primary_key = True)
	title = Column('title', String, nullable=True)
	author = Column('author', String, nullable=True)
	link = Column('link', String, nullable=True)
	content	= Column('content', String, nullable=True)
	total = Column('total', JSON, nullable=True)