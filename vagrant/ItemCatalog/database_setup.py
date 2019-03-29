import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Store(Base):
	__tablename__='store'
	
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	
class Produce(Base):
	__tablename__ = 'produce'