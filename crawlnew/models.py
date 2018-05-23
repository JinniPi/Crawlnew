from sqlalchemy.orm import sessionmaker
# from models import CrawlDB, db_connect, create_table
from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
	Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()

def db_connect():
	"""
	Performs database connection using database settings from settings.py.
	Returns sqlalchemy engine instance
	"""
	return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
	DeclarativeBase.metadata.create_all(engine)

class CrawlDB(DeclarativeBase):
	__tablename__ = "Newspaper"

	# id = Column(Integer, primary_key=True)
	origin = Column('origin',String(50))
	link = Column('link',String(1000),primary_key=True)
	title = Column('title', Text())
	sapo = Column('sapo',Text())
	content = Column('content',Text())