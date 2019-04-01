from flask import Flask,render_template, request
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Produce, ProduceItem

engine = create_engine('sqlite:///producemenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/produces/<int:produce_id>/')
def HelloWorld(produce_id):
	print(produce_id)
	return "This is the HelloWorld method."
	
@app.route('/produces/<int:produce_id>/new/', methods=['GET','POST'])
def newMenuItem(produce_id):	
	return "page to create a new produce item. Task one complete!"
	
@app.route('/produces/<int:produce_id>/<int:menuItem_id>/edit/')
def editMenuItem(produce_id,menuItem_id):
	return "page to edit a produce item. Task one complete!"
	
@app.route('/produces/<int:produce_id>/<int:menuItem_id>/delete/')	
def deleteMenuItem(produce_id,menuItem_id):
	return "page to delete a produce item. Task one complete!"
	
	
	
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port = 5000)

