import tkinter as tk
from tkinter import *
from tkinter import messagebox as tkMs

root = tk.Tk()

v = tk.IntVar()
v.set(0)

w = tk.Label(root, text=v.get())
w.pack()

def update_clock():
    v.set(v.get() + 1)
    if(v.get() < int(e.get())):
        w.configure(text=v.get())
        root.after(1000, update_clock)
    else:
        tkMs.showinfo("Wiadomość", "Final Countdown")
        v.set(0)

b1 = Button(root , text ="Start", command=update_clock)
e = Entry(root)

e.pack()
b1.pack()

root.mainloop()
