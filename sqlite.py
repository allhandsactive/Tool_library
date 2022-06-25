import sqlite3

def db_conn(filepath):
    '''Open a connection to the SQLite database file'''
    # Inuputs:
    # filepath: Location to database
    conn = sqlite3.connect(filepath)
    return conn

def db_close(conn):
    '''Close the connection'''
    # Inputs:
    # conn: SQLite connection to close
    conn.close()

def add_table(conn, name, elements):
    '''Add a new table to the database'''
    # Inputs:
    # conn: SQLite database connection
    # name: Name of the table
    # elements: dictionary where the key is the data name and the value is the data type.
    try:
        cmd = "CREATE TABLE [IF NOT EXISTS] " + name + " ( "
        for key, value in elements.items():
            cmd = cmd + key + " " + value + ", "
        cmd = cmd[:-2] + ") [WITHOUT ROWID];"

        cursor = con.cursor()
        cursor.execute(cmd)
        con.commit
    except Error as e:
        print(e)
        return False
    return True

def del_table(conn, name):
    '''Delete a table'''
    # Inputs:
    # conn: SQLite database connection
    # name: Table to be deleted
    pass

def add_user(conn, members_table, elements):
    '''Add a user to the users table'''
    # Inputs:
    # conn: SQLite database connection
    # name: Name of the table
    # elements: dictionary where the key is the data name and the value is the data type.
    pass

def del_user(conn, members_table, username):
    '''Delete a user from the users table'''
    # Inputs:
    # conn: SQLite database connection
    # members_table: table name for members
    # username: user to be removed.
    pass

def add_tool(conn, tools_table, elemenrts):
    '''Add a new tool to the tools table'''
    # Inputs:
    # conn: SQLite database connection
    # name: Name of the table
    # elements: dictionary where the key is the data name and the value is the data type.
    pass

def del_tool(conn, tools_table, name):
    '''Delete a tool from the tools table'''
    # Inputs:
    # conn: SQLite database connection
    # tools_table: table tools are stored at
    # name: tool name to be removed
    pass
