from tkinter import *
import os

#main program

def add(x,y):                                  #define function
    return x + y
def minus(x,y):
    return x - y
def multi(x,y):
    return x * y
def divide(x,y):
    return x / y
def expo(x,y):
    return x**y
def mod(x,y):
    return x%y
def f_div(x,y):
    return x//y
def root(x,y):
    return x ** (1 / y)
#GUI
main_window = Tk()
main_window.title('Calculator')
main_window.geometry('400x300')
btn_menu = Button(main_window)

main_window.mainloop()