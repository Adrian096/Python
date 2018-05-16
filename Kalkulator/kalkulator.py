import Tkinter as tk
from Tkinter import *

root = tk.Tk()

v = IntVar()
v.set(0)

vTemp = DoubleVar()
vTemp.set(0)

act = StringVar()
act.set("")

def add(op):
    text = str(v.get())+str(op)
    v.set(int(text))


def operation(op):
    if(op != "="):
        vTemp.set(v.get())
        v.set(0)
        act.set(str(op))

    if(op == "="):
        if(vTemp != 0):
            if(act.get() == "+"):
                v.set(int(vTemp.get())+int(v.get()))
                vTemp.set(0)
            elif(act.get() == "-"):
                v.set(int(vTemp.get()) - int(v.get()))
                vTemp.set(0)
            elif (act.get() == "*"):
                v.set(int(vTemp.get()) * int(v.get()))
                vTemp.set(0)
            elif (act.get() == "/"):
                v.set(int(vTemp.get()) / int(v.get()))
                vTemp.set(0)


w = Label(root, textvariable=v)
w.grid(row=0, column=0, columnspan=4)

bt1 = tk.Button(root, fg="black", text="1", command=lambda: add(1))
bt1.grid(row=1, column=0)

bt2 = tk.Button(root, fg="black", text="2", command=lambda: add(2))
bt2.grid(row=1, column=1)

bt3 = tk.Button(root, fg="black", text="3", command=lambda: add(3))
bt3.grid(row=1, column=2)

btplus = tk.Button(root, fg="black", text="+", command=lambda: operation("+"))
btplus.grid(row=1, column=3)

bt4 = tk.Button(root, fg="black", text="4", command=lambda: add(4))
bt4.grid(row=2, column=0)

bt5 = tk.Button(root, fg="black", text="5", command=lambda: add(5))
bt5.grid(row=2, column=1)

bt6 = tk.Button(root, fg="black", text="6", command=lambda: add(6))
bt6.grid(row=2, column=2)

btminus = tk.Button(root, fg="black", text="-", command=lambda: operation("-"))
btminus.grid(row=2, column=3)

bt7 = tk.Button(root, fg="black", text="7", command=lambda: add(7))
bt7.grid(row=3, column=0)

bt8 = tk.Button(root, fg="black", text="8", command=lambda: add(8))
bt8.grid(row=3, column=1)

bt9 = tk.Button(root, fg="black", text="9", command=lambda: add(9))
bt9.grid(row=3, column=2)

btmult = tk.Button(root, fg="black", text="*", command=lambda: operation("*"))
btmult.grid(row=3, column=3)

bt0 = tk.Button(root, fg="black", text="0", command=lambda: add(0))
bt0.grid(row=4, column=0)

btdot = tk.Button(root, fg="black", text=".", command=lambda: add(0))
btdot.grid(row=4, column=1)

bteq = tk.Button(root, fg="black", text="=", command=lambda: operation("="))
bteq.grid(row=4, column=2)

btdiv = tk.Button(root, fg="black", text="/", command=lambda: operation("/"))
btdiv.grid(row=4, column=3)


mainloop()