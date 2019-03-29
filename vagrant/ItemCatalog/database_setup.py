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
	
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	Store_id = Column(Integer,ForeignKey('store.id'))
	store = relationship(Store) 
	
class ProduceItem(Base):
	__tablename__ = 'menu_item'
	
	name =Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(250))
	price = Column(String(8))
	type = Column(String(250))
	produce_id = Column(Integer,ForeignKey('produce.id'))
	produce = relationship(Produce)
	
	@property
	def serialize(self):
       
		return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
           'price'         : self.price,
           'type'         : self.type,
       }
	   

	   