from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import NUMERIC
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Studenci(Base):
    __tablename__ = 'studenci'
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    surname = Column(String(100))
    book_id = Column(NUMERIC)


class Ksiazki(Base):
    __tablename__ = 'ksiazki'
    id = Column(Integer, primary_key = True)
    title = Column(String(100))
    publishing = Column(String(100))
    student_id = Column(NUMERIC)


engine = create_engine('sqlite:///liblary.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for ksiazki in session.query(Ksiazki).all():
    print(ksiazki.id, ksiazki.title, ksiazki.publishing, ksiazki.student_id)

new_data = Ksiazki(
    id = 5,
    title=u'Metro 2033',
    publishing=u'Irsing',
    student_id=1
)

new_data2 = Studenci(
    id = 2,
    name=u'Jan',
    surname=u'Kowalski',
    book_id=5
)



session.add(new_data)
session.add(new_data2)
session
