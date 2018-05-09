import Tkinter as tk
import tkFont as tkF

root = tk.Tk()

default_font = tkF.nametofont("TkDefaultFont")
default_font.configure(size=16)
root.option_add("*Font", default_font)



root.mainloop()