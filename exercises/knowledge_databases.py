from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

#var article1=article1
#var article2=article2
#var article3=article3

def add_article(name,animals,rating):
	artical_object=Knowledge(
		name=name,
		animals=animals,
		rating=rating)
	session.add(artical_object)
	session.commit()

add_article("giraffes","giraffe",8)
add_article("farrets","farret",10)
add_article("mantis shrimps","mantis shrimp", 7)

def query_all_articles():
	articles=session.query(
		Knowledge).all()
	return articles
print(query_all_articles())
for i in query_all_articles():
	print(i)


def query_article_by_topic(animal):
	article=session.query(
		Knowledge).filter_by(
		name=animal).first()
	return article
def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
