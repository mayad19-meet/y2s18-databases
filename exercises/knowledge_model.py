from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__="knowledge"
	id=Column(Integer, primary_key=True)
	name=Column(String)
	animals=Column(String)
	rating=Column(Integer)
	def __reper__(self):
		return("name: {}\n"
			"animals: {}\n"
			"rating: {}").format(
			self.name,self.animals,self.rating)

	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	pass
