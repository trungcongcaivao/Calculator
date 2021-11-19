from tkinter import Text
import tkinter
from tkinter.constants import END
from tkinter import *  # from tkinter import *

lst = ['1. a', '2. b', '3. c', '4. d']

root = Tk()
t = Text(root)
for x in lst:
    t.insert(END, x + '\n')
t.pack()
root.mainloop()