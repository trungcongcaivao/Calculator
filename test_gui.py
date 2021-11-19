from tkinter import *
import os

def second():
    new_window  = Toplevel(root)
    new_window.title("new window")
    new_window.geometry("500x500")
    lbl = Label(new_window, text="hello")
    lbl.pack()

root = Tk()
btn = Button(root, text="open second", padx=10, pady=5, fg="white", bg="#263D42", command=second)
btn.pack(padx= 20, pady= 20)
root.geometry("500x500")
root.title("main window")
root.mainloop()