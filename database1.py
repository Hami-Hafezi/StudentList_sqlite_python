import sqlite3

import os
from pprint import pprint


class database1:
    def delete():
        # create a connection object to the database file
        conn = sqlite3.connect("Students.db")

        # create a cursor object
        cur = conn.cursor()

        # execute a DELETE statement

        cur.execute("""DROP TABLE IF EXISTS students;""")

        # commit the changes
        conn.commit()

        # close the connection
        conn.close()

    def createTable(self):
        connection1 = sqlite3.connect("Students.db")

        cursorForStudent = connection1.cursor()

        # Creating table
        table = """     CREATE TABLE IF NOT EXISTS students (
            firstName TEXT NOT NULL,
            lastName TEXT NOT NULL,
            uniNumber INTEGER UNIQUE,
            PRIMARY KEY("uniNumber")
                ); """

        cursorForStudent.execute(table)
        cursorForStudent.execute("""ALTER TABLE students ADD COLUMN normalNumber1 INTEGER;""")
        cursorForStudent.execute("""ALTER TABLE students ADD COLUMN normalNumber2 INTEGER;""")
        cursorForStudent.execute("""ALTER TABLE students ADD COLUMN normalNumber3 INTEGER;""")
        cursorForStudent.execute("""ALTER TABLE students ADD COLUMN normalNumber4 INTEGER;""")
        cursorForStudent.execute("""ALTER TABLE students ADD COLUMN normalNumber5 INTEGER;""")
        cursorForStudent.execute("""ALTER TABLE students ADD COLUMN spcNumber1 INTEGER;""")
        cursorForStudent.execute("""ALTER TABLE students ADD COLUMN spcNumber2 INTEGER;""")
        cursorForStudent.execute("""ALTER TABLE students ADD COLUMN spcNumber3 INTEGER;""")
        cursorForStudent.execute("""ALTER TABLE students ADD COLUMN spcNumber4 INTEGER;""")
        cursorForStudent.execute("""ALTER TABLE students ADD COLUMN spcNumber5 INTEGER;""")
        print("Table is Ready")

        cursorForStudent.close()

    def print_db(self):
        conn = sqlite3.connect("Students.db")

        cur = conn.cursor()

        cur.execute("SELECT * FROM students")

        results = cur.fetchall()

        pprint(results)

        conn.close()

    def getStudentFromUniNumber(uniNumberForWorkWithStudentInDataBase):
        conn = sqlite3.connect("Students.db")

        cur = conn.cursor()
        sqlite = '"SELECT FROM students where uniNumber = ?"'
        cur.execute(sqlite, (uniNumberForWorkWithStudentInDataBase,))

        results = cur.fetchall()

        conn.close()
        return results
