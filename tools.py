#!/usr/bin/env python3
from sqlite import *
from tkinter import *
import sys

def new_table():
    conn = db_conn("test.db")
    table_name = "users"
    table_elements = {"Username":"text", "fname":"text", "lname":"text"}
    add_table(conn, table_name, table_elements)

def window():
    root = Tk()
    root.config(menu=menuing(root))
    root.mainloop()

def menuing(window):
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open Database")
    filemenu.add_command(label="Save Database")
    filemenu.add_command(label="Export")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    return menubar

def main():
    window()

if __name__ =="__main__":
    main()
