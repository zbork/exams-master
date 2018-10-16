from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
users_engine = create_engine('sqlite:///users.db', echo=True)
Base = declarative_base()
 

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	username = Column(String)


	def __init__(self, username):
		self.username = username
 
# create tables
Base.metadata.create_all(users_engine)