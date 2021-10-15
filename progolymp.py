from tkinter import *
from tkinter import ttk


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="1").grid(column=0, row=0)
ttk.Label(frm, text="2").grid(column=1, row=0)
ttk.Label(frm, text="3").grid(column=2, row=0)
ttk.Label(frm, text="4").grid(column=0, row=1)
ttk.Label(frm, text="5").grid(column=1, row=1)
ttk.Label(frm, text="6").grid(column=2, row=1)
ttk.Label(frm, text="7").grid(column=0, row=2)
ttk.Label(frm, text="8").grid(column=1, row=2)
ttk.Label(frm, text="9").grid(column=2, row=2)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
root.mainloop()


#   x = int(input('X value: '))
#   y = int(input('Y value: '))
