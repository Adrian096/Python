import tkinter as tk
from tkinter import *
from tkinter.filedialog import *

root = tk.Tk()

def save():
    text = textArea.get("1.0", END)
    f = tk.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    f.write(text)
    f.close()
    
def open():
    f = tk.filedialog.askopenfile(filetypes=(('text files', '.txt'),))
    if f is None:
        return
    
    textArea.delete('1.0', END)
    textArea.insert(INSERT, f.read())
    
def setFont():
    f = listbox.get(ACTIVE)
    textArea.config(font=('Verdana', f))

    
root.geometry("700x500")

root.grid_propagate(False)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

scroll = Scrollbar(root)
textArea = Text(root)
scroll.grid(row=0, column=3, sticky='nsw')
textArea.grid(row=0, column=0, columnspan=3, sticky='nsew')
scroll.config(command=textArea.yview)
textArea.config(yscrollcommand=scroll.set, font=('Verdana', 15))



b1 = Button(root, text="Save", command=lambda: save())
b1.grid(row=1, column=0)
b2 = Button(root, text="Set font", command=lambda: setFont())
b2.grid(row=1, column=1)
b3 = Button(root, text="Open", command=lambda: open())
b3.grid(row=1, column=2)

listbox = Listbox(root)
listbox.grid(row=1, column=3)

for item in [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]:
    listbox.insert(END, item)


root.mainloop()
