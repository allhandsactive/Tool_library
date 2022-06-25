import sqlite3

def db_conn(filepath):
    conn = sqlite3.connect(filepath)
    return conn

def db_close(conn):
    conn.close()

def add_table(conn, name, elements):
    pass

def del_table(conn, name):
    pass

def add_user(conn, members_table, elements):
    pass

def del_user(conn, members_table, username):
    pass

def add_tool(conn, tools_table, elemenrts):
    pass

def del_tool(conn, tools_table, name):
    pass
