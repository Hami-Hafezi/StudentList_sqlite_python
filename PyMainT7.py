import os
import sqlite3

import database1


class student():
    def __init__(self, firstName, lastName, UCode, studyNormalLessonsList, studySpecificLessons):
        self.fostName2 = firstName
        self.lastName2 = lastName
        self.UCode2 = UCode
        self.studyNormalLessonsList2 = studyNormalLessonsList
        self.studySpecificLessons2 = studySpecificLessons


def insertVaribleIntoTable(firstName, lastName, uniNumber, normalNumber1, normalNumber2, normalNumber3,
                           normalNumber4,
                           normalNumber5, spcNumber1, spcNumber2, spcNumber3, spcNumber4, spcNumber5):
    if os.path.exists("Students.db"):
        # Create a connection object to the database file
        sqliteConnection = sqlite3.connect('Students.db')
        # Set the trace callback to print the SQL statements
        sqliteConnection.set_trace_callback(print)
        # Create a cursor object
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # Try to execute the INSERT statement
        try:
            cursor.execute(
                "INSERT INTO students (firstName ,lastName ,uniNumber ,normalNumber1 ,normalNumber2 ,normalNumber3 ,normalNumber4 , normalNumber5, spcNumber1, spcNumber2, spcNumber3, spcNumber4, spcNumber5) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (firstName, lastName, uniNumber, normalNumber1, normalNumber2, normalNumber3, normalNumber4,
                 normalNumber5,
                 spcNumber1, spcNumber2, spcNumber3, spcNumber4, spcNumber5))
            print("Python Variables inserted successfully into students table table")
            # Save the changes to the database
            sqliteConnection.commit()
        # Catch any exceptions that might occur

        except sqlite3.Error as e:
            print("Error occurred:", e.args[0])
        # Close the cursor and the connection objects
        finally:

            cursor.close()

        sqliteConnection.commit()
        sqliteConnection.close()
    else:
        print("Database file does not exist")

def main():

    print(
        "Choose your choice for operation\n\n 1_Add Student to list\n\n 2_delete Student from list \n\n 3_Edit Student perapeties with geting UniCode:\n\n 4 Calucate and print full name and exam results and Average normal and avarage specific exam numbers\n\n 5_List of bad Studente(12+) \n\n 6_list of Good Students(17+) \n\n 7_list of between exma number average \n\n 8_full result of all students \n\n 9_exit\n\n"
        " 10_delete db")
    getnumber = int(input("tell me : the number : "))
    if getnumber == 1:

        i = 1
        studentCount = int(input("tell me the number of Students : "))

        while True:

            print(
                "tell me the 1-FirstName 2-LastName 3-UniCode with 5 digits 4-tell me the 5 normal exam numbers 5-tell me 5 specific Exam numbers")
            # normal number = droose Omoomi
            # SpecificNumber = doroos ekhtesasy
            getFirstName = str(input("FirstName : "))
            getLastName = str(input("LastName : "))
            getUniversityCode = int(input("UniversityCode with 5 digit : "))
            getNormalExamNumber1 = int(input("normal 1 : "))
            getNormalExamNumber2 = int(input("normal 2 : "))
            getNormalExamNumber3 = int(input("normal 3 : "))
            getNormalExamNumber4 = int(input("normal 4 : "))
            getNormalExamNumber5 = int(input("normal 5 : "))
            getSpecificNumber1 = int(input("specific 1 : "))
            getSpecificNumber2 = int(input("specific 2 : "))
            getSpecificNumber3 = int(input("specific 3 : "))
            getSpecificNumber4 = int(input("specific 4 : "))
            getSpecificNumber5 = int(input("specific 5 : "))
            insertVaribleIntoTable(getFirstName, getLastName, getUniversityCode, getNormalExamNumber1,
                                   getNormalExamNumber2, getNormalExamNumber3, getNormalExamNumber4,
                                   getNormalExamNumber5, getSpecificNumber1, getSpecificNumber2, getSpecificNumber3,
                                   getSpecificNumber4, getSpecificNumber5)
            print("student {} inserted to table \n", format(i))

            if i == studentCount:
                break
            i += 1

        obj.print_db()
        main()
    elif getnumber == 2:
        numberForDeleteStudent = int(input("tell me the student uniNumber for delete his/her : "))

        def deleteStudentFromStudentsTable():
            conn = sqlite3.connect("Students.db")

            cur = conn.cursor()
            #  sqlite = '"SELECT FROM students where uniNumber = ?"'
            #  cur.execute(sqlite, (uniNumberForWorkWithStudentInDataBaseAndDelete,))
            #  result = cur.fetchall()
            sql_update_query = """DELETE from students where uniNumber = ?"""
            cur.execute(sql_update_query, (numberForDeleteStudent,))
            conn.commit()

        # cur.execute("""ALTER TABLE students DROP ROW normalNumber1 where uniNimber = ?;""")
        obj.print_db()

        print("Student deleted from studensts table")
        main()
    elif getnumber == 8:
        obj.print_db()
        main()
    elif getnumber == 9:
        exit(0)
    elif getnumber == 10:
        database1.database1.delete()


# cursorForStudent.execute("SELECT * FROM students")

database1.database1.delete()
obj = database1.database1()
obj.createTable()
main()
