import sqlite3

class sqlite_work:
    def __init__(self):
        self.conn = None

    def db_conn(self, filepath):
        '''Open a connection to the SQLite database file'''
        # Inuputs:
        # filepath: Location to database
        self.conn = sqlite3.connect(filepath)

    def db_close(self):
        '''Close the connection'''
        # Inputs:
        # conn: SQLite connection to close
        self.conn.close()

    def add_table(self, name, elements):
        '''Add a new table to the database'''
        # Inputs:
        # conn: SQLite database connection
        # name: Name of the table
        # elements: dictionary where the key is the data name and the value is the data type.
        try:
            cur = self.conn.cursor()
            cmd = "CREATE TABLE [IF NOT EXISTS] " + name + " ( "
            for key, value in elements:
                cmd = cmd + key + " " + value + ", "
            cmd = cmd[:-2] + " )[WITHOUT ROWID];"
            cur.execute(cmd)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def del_table(self, name):
        '''Delete a table'''
        # Inputs:
        # conn: SQLite database connection
        # name: Table to be deleted
        try:
            cur = self.conn.cursor()
            cmd = "DROP TABLE [IF EXISTS] " + name
            cur.execute(cmd)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def add_user(self, members_table, elements):
        '''Add a user to the users table'''
        # Inputs:
        # conn: SQLite database connection
        # name: Name of the table
        # elements: Array of arrays to get user info
        try:
            cur = self.conn.cursor()
            for element in element:
                cmd = "INSERT INTO " + members_table + " VALUES ( "
                for ele in element:
                    cmd = cmd + ele + ", "
                cmd = cmd[:-2] + ");"
                cur.execute(cmd)
                self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def del_user(self, members_table, username):
        '''Delete a user from the users table'''
        # Inputs:
        # conn: SQLite database connection
        # members_table: table name for members
        # username: user to be removed.
        cmd = "DELETE FROM " + members_table + " WHERE username = " + username
        try:
            cur = self.conn.cursor()
            cur.execute(cmd)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def add_tool(self, tools_table, elemenrts):
        '''Add a new tool to the tools table'''
        # Inputs:
        # conn: SQLite database connection
        # name: Name of the table
        # elements: dictionary where the key is the data name and the value is the data type.
        try:
            cur = self.conn.cursor()
            for element in element:
                cmd = "INSERT INTO " + tools_table + " VALUES ( "
                for ele in element:
                    cmd = cmd + ele + ", "
                cmd = cmd[:-2] + ");"
                cur.execute(cmd)
                self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def del_tool(self, tools_table, name):
        '''Delete a tool from the tools table'''
        # Inputs:
        # conn: SQLite database connection
        # tools_table: table tools are stored at
        # name: tool name to be removed
        cmd = "DELETE FROM " + tools_table + " WHERE username = " + name
        try:
            cur = self.conn.cursor()
            cur.execute(cmd)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
