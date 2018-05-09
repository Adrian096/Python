import Tkinter as tk
import tkFont as tkF
import time as tm

root = tk.Tk()

default_font = tkF.nametofont("TkDefaultFont")
default_font.configure(size=16)
root.option_add("*Font", default_font)

i = 20

for i in range(0, 20):
    i = i+1
    tm.sleep(1000)
    print(i)

