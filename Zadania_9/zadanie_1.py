import Tkinter as tk
import tkMessageBox as tkM

root = tk.Tk()
v = tk.StringVar()
v.set("red")

def readValue():
    bt.config(fg=v.get())

def echo():
    tkM.showinfo("Wiadomosc", "info")

rb1 = tk.Radiobutton(root, text="Red", variable=v, value="red", command=readValue)
rb1.grid(column=0, row=0)

rb2 = tk.Radiobutton(root, text="Blue", variable=v, value="green", command=readValue)
rb2.grid(column=1, row=0)

rb3 = tk.Radiobutton(root, text="Green", variable=v, value="blue", command=readValue)
rb3.grid(column=3, row=0)

bt = tk.Button(root, fg="red", text="BUTTON", command=echo)
bt.grid(row=1,column=0, columnspan=3)

root.mainloop()