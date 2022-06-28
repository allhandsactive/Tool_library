#!/usr/bin/env python3
from tkinter import *
from sqlite import *
import sys

def window():
    db = sqlite_work()
    root = Tk()
    root.geometry('500x500')
    root.config(menu=menuing(root, db))
    main_window(root, db)
    root.mainloop()

def menuing(window, db):
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open Database", command=db.db_conn("/home/daemoneye/.tools/aha.db"))
    filemenu.add_command(label="Export")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.destroy)
    menubar.add_cascade(label="File", menu=filemenu)

    return menubar

def main_window(window, db):
    checkout_item = Button(window, text = "Checkout a tool")
    return_item = Button(window, text = "Return a tool")
    checkout_item.pack()
    return_item.pack()

def main():
    window()

if __name__ =="__main__":
    main()
