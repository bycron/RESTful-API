import sqlite3
from sqlite3 import Error

class Table:
    def __init__(self, tablename, tableargs, dbname='data.db'):
        self.dbname = dbname
        self.tablename = tablename
        self.tableargs = tableargs

        self.connection = None
        self.cursor = None

        self.__create__connection()

    def __del__(self):
        if self.connection:
            self.connection.commit()
            self.connection.close()

    def __create__connection(self):
        try:
            creation_query = f"CREATE TABLE IF NOT EXISTS {self.tablename} ({self.tableargs})"

            self.connection = sqlite3.connect(self.dbname)
            self.cursor = self.connection.cursor()
            self.cursor.execute(creation_query)
        except Error as e:
            print(e)

    def insert_values(self, values):
        insert_query = f"INSERT INTO {self.tablename} VALUES ({values})"
        self.cursor.execute(insert_query)


