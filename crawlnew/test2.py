from sqlalchemy.orm import sessionmaker
# from models import CrawlDB, db_connect, create_table
from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
	Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

#from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()

def db_connect():
	"""
	Performs database connection using database settings from settings.py.
	Returns sqlalchemy engine instance
	"""
	return create_engine('mysql://root:12345@localhost:3306/crawlnew')

def create_table(engine):
	DeclarativeBase.metadata.create_all(engine)

class CrawlDB(DeclarativeBase):
	__tablename__ = "Newspaper"

	id = Column(Integer, primary_key=True)
	origin = Column('origin',String(50))
	link = Column('link', Text())
	title = Column('title', Text())
	sapo = Column('sapo',Text())
	content = Column('content',Text())
engine = db_connect()
#create_table(engine)
Session = sessionmaker(bind=engine)
sets = set()
session = Session()
quotedb = CrawlDB()
try:
	session.commit()

	#query again
	list_obj = session.query(CrawlDB).all()
	print(type(list_obj))
	print(list_obj[0].link)
	for obj in list_obj:
		sets.add(obj.link)
		print(obj.link)
	print(sets)
except:
	session.rollback()
	raise
finally:
	session.close()