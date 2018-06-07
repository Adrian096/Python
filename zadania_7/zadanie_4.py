from sqlalchemy import Column, Integer, String
from sqlalchemy.types import NUMERIC
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Studenci(Base):
    __tablename__ = 'studenci'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(100))
    surname = Column(String(100))
    book_id = Column(NUMERIC)


class Ksiazki(Base):
    __tablename__ = 'ksiazki'
    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String(100))
    publishing = Column(String(100))
    student_id = Column(NUMERIC)


engine = create_engine('sqlite:///library.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def wyswietlTabele(ch=0):
    print("Wybierz tabele:")
    print("1.Ksiazki")
    print("2.Studenci")
    if(ch == 0):
        choose = int(input("Wybierz: "))
    else:
        choose = ch

    if (choose == 1):
        for ksiazki in session.query(Ksiazki).all():
            print(ksiazki.id, ksiazki.title, ksiazki.publishing, ksiazki.student_id)
    elif (choose == 2):
        for studenci in session.query(Studenci).all():
            print(studenci.id, studenci.name, studenci.surname, studenci.book_id)

def dodajRekord():
    print("Wybierz tabele:")
    print("1.Ksiazki")
    print("2.Studenci")

    choose = int(input("Wybierz: "))

    if(choose == 1):
        title = input("Tytuł: ")
        publishing = input("Wydawca: ")
        new_data = Ksiazki(
            title = title,
            publishing = publishing
        )
        session.add(new_data)
        session.commit()
    elif(choose == 2):
        name = input("Imie: ")
        surname = input("Nazwisko: ")
        new_data = Studenci(
            name = name,
            surname = surname
        )
        session.add(new_data)
        session.commit()


def usunRekord():
    print("Wybierz tabele:")
    print("1.Ksiazki")
    print("2.Studenci")

    choose = int(input("Wybierz: "))
    if (choose == 1):
        print("Wyswietlic tabele?")
        print("1.TAK")
        print("2.NIE")
        w = int(input("TAK-1/NIE-2: "))
        if (w == 1):
            wyswietlTabele(1)

        idDel = int(input("Podaj id: "))

        obj = session.query(Ksiazki).filter_by(id=idDel).one()
        session.delete(obj)
        session.commit()
    elif(choose == 2):
        print("Wyswietlic tabele?")
        print("1.TAK")
        print("2.NIE")
        w = int(input("TAK-1/NIE-2: "))
        if (w == 1):
            wyswietlTabele(2)

        idDel = int(input("Podaj id: "))
        obj = session.query(Studenci).filter_by(id=idDel).one()
        session.delete(obj)
        session.commit()


def wypozyczona():
    print("Wyswietlic tabele?")
    print("1.TAK")
    print("2.NIE")
    w = int(input("TAK-1/NIE-2: "))
    if (w == 1):
        wyswietlTabele(1)
        wyswietlTabele(2)
    idK = int(input("Podaj id książki"))
    idS = int(input("Podaj id studenta"))

    ksiazka = session.query(Ksiazki).filter_by(id=idK).one()
    student = session.query(Studenci).filter_by(id=idS).one()
    ksiazka.student_id = idS
    student.book_id = idK
    session.commit()

choose = 0

while(choose != 9):
    print("Wybierz działanie")
    print("1.dodaj rekord do bazy danych")
    print("2.usuń rekord z bazy danych")
    print("3.wyswietl tabele")
    print("4.ustaw wypozyczenie")
    choose = int(input("działanie: "))

    if(choose == 1):
        dodajRekord()
    elif(choose == 2):
        usunRekord()
    elif(choose == 3):
        wyswietlTabele()
    elif(choose == 4):
        wypozyczona()


