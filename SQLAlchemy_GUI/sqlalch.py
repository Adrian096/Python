from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import tkinter as tk
from tkinter import messagebox

Base = declarative_base()

root = tk.Tk()

root.grid_propagate(False)


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.nameLabel = tk.Label(self.frame, text="Name")
        self.nameLabel.grid(row=0, column=0)

        self.nameArea = tk.Entry(self.frame)
        self.nameArea.grid(row=0, column=1)

        self.surnameLabel = tk.Label(self.frame, text="Surname")
        self.surnameLabel.grid(row=1, column=0)

        self.surnameArea = tk.Entry(self.frame)
        self.surnameArea.grid(row=1, column=1)

        self.albumLabel = tk.Label(self.frame, text="Album number")
        self.albumLabel.grid(row=2, column=0)

        self.albumArea = tk.Entry(self.frame)
        self.albumArea.grid(row=2, column=1)

        self.b1 = tk.Button(self.frame, text='Add', command=self.add)
        self.b1.grid(row=3, column=0)

        self.b2 = tk.Button(self.frame, text='Show data', command=self.show)
        self.b2.grid(row=3, column=1)

        self.frame.grid()

    def add(self):
        name = self.nameArea.get()
        surname = self.surnameArea.get()
        album = self.albumArea.get()

        if(not name or not surname or not album):
            messagebox.showinfo("Error", "Fields cannot be empty!")
            return
        else:
            new_user = Student(name=name, surname=surname, album_no=album)
            sesssion.add(new_user)
            sesssion.commit()

    def show(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = ShowTable(self.newWindow)


class ShowTable:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.frame.grid()
        self.data = sesssion.query(Student).all()
        self.init()

    def init(self):

        tk.Label(self.frame, text="Name", borderwidth=2, relief="groove").grid(row=0, column=0)
        tk.Label(self.frame, text="Surname", borderwidth=2, relief="groove").grid(row=0, column=1)
        tk.Label(self.frame, text="Album", borderwidth=2, relief="groove").grid(row=0, column=2)

        i = 1
        for x in self.data:
            tk.Label(self.frame, text=x.name, borderwidth=2, relief="groove").grid(row=i, column=0)
            tk.Label(self.frame, text=x.surname, borderwidth=2, relief="groove").grid(row=i, column=1)
            tk.Label(self.frame, text=x.album_no, borderwidth=2, relief="groove").grid(row=i, column=2)
            tk.Button(self.frame, text="Remove", command=lambda: self.remove(x.id)).grid(row=i, column=3)
            i+=1


    def remove(self, id):
        student = sesssion.query(Student).filter_by(id=id).first()
        sesssion.delete(student)
        sesssion.commit()
        self.init()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    album_no = Column(Integer)

    def __init__(self, name, surname, album_no):
        self.name = name
        self.surname = surname
        self.album_no = album_no


engine = create_engine('sqlite:///students.db', echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

sesssion = Session()

MainWindow(root)

tk.mainloop()