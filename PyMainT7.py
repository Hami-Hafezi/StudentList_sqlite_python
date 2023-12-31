# HamiHAfeziArdakani
import os
import sqlite3
from turtledemo.chaos import f

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
                           normalNumber5, spcNumber1, spcNumber2, spcNumber3, spcNumber4, spcNumber5, ave1, ave2,
                           aveAll):
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
                "INSERT INTO students (firstName ,lastName ,uniNumber ,normalNumber1 ,normalNumber2 ,normalNumber3 ,normalNumber4 , normalNumber5, spcNumber1, spcNumber2, spcNumber3, spcNumber4, spcNumber5,ave1,ave2,aveAll) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (firstName, lastName, uniNumber, normalNumber1, normalNumber2, normalNumber3, normalNumber4,
                 normalNumber5,
                 spcNumber1, spcNumber2, spcNumber3, spcNumber4, spcNumber5, ave1, ave2, aveAll))
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
        "Choose your choice for operation\n\n 1_Add Student to list\n\n 2_delete Student from list \n\n 3_Edit Student perapeties with geting UniCode:\n\n 4 Calucate and print full name and exam results and Average normal and avarage specific exam numbers\n\n 5_List of bad Studente(12+) \n\n 6_ nomerata marboot be yek dars az hame daneshjooyan\n\n 7_list of Good Students(17+) \n\n 8_list of between exma number average \n\n 9_full result of all students \n\n 10_exit\n\n"
        " 11_delete db")
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
            ave1 = (
                           getNormalExamNumber1 + getNormalExamNumber2 + getNormalExamNumber3 + getNormalExamNumber4 + getNormalExamNumber5) / 5
            ave2 = (
                           getSpecificNumber1 + getSpecificNumber2 + getSpecificNumber3 + getSpecificNumber4 + getSpecificNumber5) / 5
            aveAll = (ave1 + ave2) / 2

            insertVaribleIntoTable(getFirstName, getLastName, getUniversityCode, getNormalExamNumber1,
                                   getNormalExamNumber2, getNormalExamNumber3, getNormalExamNumber4,
                                   getNormalExamNumber5, getSpecificNumber1, getSpecificNumber2, getSpecificNumber3,
                                   getSpecificNumber4, getSpecificNumber5, ave1, ave2, aveAll)
            print("student {} inserted to table \n", format(i))

            if i == studentCount:
                break
            i += 1

        obj.print_db()
        main()
    elif getnumber == 2:
        # Remove
        def RemoveAllWithGetUniNumber(uniNumberForRemove):
            conn = sqlite3.connect("Students.db")

            cur = conn.cursor()
            #  sqlite = '"SELECT FROM students where uniNumber = ?"'
            #  cur.execute(sqlite, (uniNumberForWorkWithStudentInDataBaseAndDelete,))
            #  result = cur.fetchall()
            sql_remove_query = """DELETE from students where uniNumber = ?"""
            cur.execute(sql_remove_query, (uniNumberForRemove,))
            conn.commit()

        RemoveAllWithGetUniNumber(int(input("tell me a number for delete3")))
        obj.print_db()
        main()
    elif getnumber == 3:
        numberForDeleteStudent = int(input("tell me the student uniNumber for Edit his/her properties : "))

        def replace(uniNumberGet):
            conn = sqlite3.connect("Students.db")
            cur = conn.cursor()
            newFirstName = (input("tell me new FirstName"))
            newLastName = (input("tell me new lastName"))
            newNuinumber = int(input("tell me new uninumber"))
            newNormalNumber1 = int(input("tell me new normalNumber 1 : "))
            newNormalNumber2 = int(input("tell me new normalNumber 2 : "))
            newNormalNumber3 = int(input("tell me new normalNumber 3 : "))
            newNormalNumber4 = int(input("tell me new normalNumber 4 : "))
            newNormalNumber5 = int(input("tell me new normalNumber 5 : "))
            newSpcNumber1 = int(input("tell me new spcNumber 1 : "))
            newSpcNumber2 = int(input("tell me new spcNumber 2 : "))
            newSpcNumber3 = int(input("tell me new spcNumber 3 : "))
            newSpcNumber4 = int(input("tell me new spcNumber 4 : "))
            newSpcNumber5 = int(input("tell me new spcNumber 5 : "))

            cur.execute(
                "UPDATE students SET uniNumber = ?, firstName = ?, lastName = ?, normalNumber1 = ?,normalNumber2 = ?,normalNumber3 = ?,normalNumber4 = ?,normalNumber5 = ?,spcNumber1 = ?,spcNumber2 = ?,spcNumber3 = ?,spcNumber4 = ?,spcNumber5 = ? WHERE uniNumber = ?",
                (newNuinumber, newFirstName, newLastName, newNormalNumber1, newNormalNumber2, newNormalNumber3,
                 newNormalNumber4, newNormalNumber5, newSpcNumber1, newSpcNumber2, newSpcNumber3, newSpcNumber4,
                 newSpcNumber5, uniNumberGet,))

            # cur.execute("UPDATE students SET firstName = ? WHERE uniNumber = ?", (newFirstName,uniNumberGet,))
            # cur.execute("UPDATE students SET lastName = ? WHERE uniNumber = ?", (newLastName,uniNumberGet,))
            # cur.execute("UPDATE students SET uniNumber = ? WHERE uniNumber = ?", (newNuinumber,uniNumberGet,))
            # cur.execute("UPDATE students SET uniNumber = ? WHERE uniNumber = ?", (newNuinumber,uniNumberGet,))
            # cur.execute("UPDATE students SET uniNumber = ? WHERE uniNumber = ?", (newNuinumber,uniNumberGet,))
            # cur.execute("UPDATE students SET uniNumber = ? WHERE uniNumber = ?", (newNuinumber,uniNumberGet,))
            # cur.execute("UPDATE students SET uniNumber = ? WHERE uniNumber = ?", (newNuinumber,uniNumberGet,))
            # cur.execute("UPDATE students SET uniNumber = ? WHERE uniNumber = ?", (newNuinumber,uniNumberGet,))
            # cur.execute("UPDATE students SET uniNumber = ? WHERE uniNumber = ?", (newNuinumber,uniNumberGet,))
            # cur.execute("UPDATE students SET uniNumber = ? WHERE uniNumber = ?", (newNuinumber,uniNumberGet,))
            # cur.execute("UPDATE students SET uniNumber = ? WHERE uniNumber = ?", (newNuinumber,uniNumberGet,))
            # cur.execute("UPDATE students SET uniNumber = ? WHERE uniNumber = ?", (newNuinumber,uniNumberGet,))

            conn.commit()
            cur.close()
            conn.close()

        replace(numberForDeleteStudent)
        # cur.execute("""ALTER TABLE students DROP ROW normalNumber1 where uniNimber = ?;""")
        obj.print_db()

        print("Student deleted from studensts table")
        main()
    #   elif getnumber == 4:
    # def editTableWithGetUniNumber(uniNumberForEdit):
    #     conn = sqlite3.connect("Students.db")
    #     cur = conn.cursor()
    #     getFirstName = str(input("FirstName : "))
    #     getLastName = str(input("LastName : "))
    #     getUniversityCode = int(input("UniversityCode with 5 digit : "))
    #     getNormalExamNumber1 = int(input("normal 1 : "))
    #     getNormalExamNumber2 = int(input("normal 2 : "))
    #     getNormalExamNumber3 = int(input("normal 3 : "))
    #     getNormalExamNumber4 = int(input("normal 4 : "))
    #     getNormalExamNumber5 = int(input("normal 5 : "))
    #     getSpecificNumber1 = int(input("specific 1 : "))
    #     getSpecificNumber2 = int(input("specific 2 : "))
    #     getSpecificNumber3 = int(input("specific 3 : "))
    #     getSpecificNumber4 = int(input("specific 4 : "))
    #     getSpecificNumber5 = int(input("specific 5 : "))
    #     # execute the query
    #     cur.execute(
    #         "UPDATE students SET firstName  = ?, lastName = ?,uniNumber  = ?, normalNumber1 = ?,normalNumber2  = ?, normalNumber3 = ?,normalNumber4  = ?, normalNumber5 = ?,spcNumber1  = ?, spcNumber2 = ?,spcNumber3  = ?, spcNumber4 = ?,spcNumber5 = ? WHERE uniNumber = ?",
    #         (getFirstName, getLastName, getUniversityCode,getNormalExamNumber1,getNormalExamNumber2, getNormalExamNumber3,getNormalExamNumber4, getNormalExamNumber5,getSpecificNumber1, getSpecificNumber2,getSpecificNumber3, getSpecificNumber4,getSpecificNumber5, uniNumberForEdit))
    #     obj.print_db()
    #     # commit the changes
    #     conn.commit()
    #
    #     # close the connection
    #     conn.close()
    #
    # editTableWithGetUniNumber(int(input("tell me a number for edit")))
    # obj.print_db()
    # main()
    elif getnumber == 4:
        # printKhosusiat
        def printKhosusiatWithGetUniNumber(uniNumebrGet):
            conn1 = sqlite3.connect("Students.db")

            # create a cursor object
            cur1 = conn1.cursor()
            # execute the query
            cur1.execute("SELECT * FROM students WHERE uniNumber = ?", (uniNumebrGet,))

            #
            results = cur1.fetchall()
            normalNumbersSum = 0
            spcNumbersSum = 0

            for row in results:
                normalNumbersSum = normalNumbersSum + row[3] + row[4] + row[5] + row[6] + row[7]
                spcNumbersSum = spcNumbersSum + row[8] + row[9] + row[10] + row[11] + row[12]
                print("full name is {} {}".format(row[0], row[1]))
                print("uniNumber is {}".format(row[2]))
            aveNormalNumbers = normalNumbersSum / 5
            aveSpcNumbers = spcNumbersSum / 5
            print("average of normalNumbers is : {}".format(aveNormalNumbers))
            print("average of specificNumbers is : {}".format(aveSpcNumbers))
            # close the connection
            cur1.close()
            conn1.close()

            # cur1.execute("SELECT * FROM students WHERE uniNumber = ?", (uniNumebrGet,))
            #
            # #
            # results = cur1.fetchall()
            # for row in results:
            #     normalNumbersSum = normalNumbersSum + row[3] + row[4] + row[5] + row[6] + row[7]
            #     spcNumbersSum = spcNumbersSum + row[8] + row[9] + row[10] + row[11] + row[12]
            #     print("full name is {} {}".format(row[0], row[1]))
            #     print("uniNumber is {}".format(row[2]))
            # aveNormalNumbers = normalNumbersSum / 5
            # aveSpcNumbers = spcNumbersSum / 5
            # for row in results:
            #     avarageOfaveSpcNumbersAndSpcNumbers= (aveSpcNumbers + aveNormalNumbers)/2
            #     cur1.execute("SELECT * FROM my_table WHERE ? < ?", (avarageOfaveSpcNumbersAndSpcNumbers,12,))
            #
            # if avarageOfaveSpcNumbersAndSpcNumbers < 12:
            #     print("bad studnet(mashroot) ")
            #
            # else:
            #     print("good studnet(mashroot nashode) ")
            # print("average of normalNumbers is : {}".format(aveNormalNumbers))
            # print("average of specificNumbers is : {}".format(aveSpcNumbers))

        printKhosusiatWithGetUniNumber(int(input("tell me a number for print")))
        main()
    elif getnumber == 5:
        # Print Mashrooti Ha(13-)
        def printMashrootinList():
            conn1 = sqlite3.connect("Students.db")

            cur1 = conn1.cursor()

            cur1.execute(
                "SELECT firstName, Case when aveAll < 12 THEN 'Mashroot' Else 'mashroot nist' END as 'uniExamNumbers' FROM students ", )
            results = cur1.fetchall()
            filtered_results = [row for row in results if row[1] == 'Mashroot']
            for row in filtered_results:
                print(row[0])
            cur1.close()
            conn1.close()

        printMashrootinList()
        main()
    elif getnumber == 6:
        getDars = int(input(
            "tell me one normal number or specific number its :normal number [0 ta 4] specific number [5 ta 9] "))

        def printAllStudnetsInListWithGetOneNoramelOrSpcNumber(getdarsNumber):
            conn1 = sqlite3.connect("Students.db")

            cur1 = conn1.cursor()
            # numberField = ""
            # if getdarsNumber == 0:
            #     numberField = "normalNumber1"
            # elif getdarsNumber == 1:
            #     numberField = "normalNumber1"
            # elif getdarsNumber == 2:
            #     numberField = "normalNumber1"
            # elif getdarsNumber == 3:
            #     numberField = "normalNumber1"
            # elif getdarsNumber == 4:
            #     numberField = "normalNumber1"
            # elif getdarsNumber == 5:
            #     numberField = "spcNumber1"
            # elif getdarsNumber == 6:
            #     numberField = "spcNumber2"
            # elif getdarsNumber == 7:
            #     numberField = "spcNumber3"
            # elif getdarsNumber == 8:
            #     numberField = "spcNumber4"
            # elif getdarsNumber == 9:
            #     numberField = "spcNumber5"
            # else:
            #     print("not found")
            # cur1.execute(
            # "SELECT * FROM students,WHERE {column_name} IS ?", (numberField, numberField,))

            # execute the query
            cur1.execute("SELECT ? FROM students", (getdarsNumber,))

            # fetch the results
            results = cur1.fetchall()

            # print the results
            for row in results:
                print(row)

            cur1.close()
            conn1.close()

        printAllStudnetsInListWithGetOneNoramelOrSpcNumber(getDars)
        main()
    elif getnumber == 7:
        # Print Momtaz Ha(17+)
        def printMomtazinList():
            conn1 = sqlite3.connect("Students.db")

            cur1 = conn1.cursor()
            cur1.execute(
                "SELECT firstName, Case when aveAll >= 17 THEN 'Momtaz' Else 'momtaz nist' END as 'uniExamNumbers' FROM students ", )
            results = cur1.fetchall()
            filtered_results = [row for row in results if row[1] == 'Momtaz']
            for row in filtered_results:
                print(row[0])
            cur1.close()
            conn1.close()

        printMomtazinList()
        main()
    elif getnumber == 8:
        addBozorg1 = int(input("tell me add bozorg"))
        addkoochak1 = int(input("tell me add koochak"))

        def PerintUserinputBetweenTwoNumber(addBozorg, addKoochak):
            conn1 = sqlite3.connect("Students.db")

            cur1 = conn1.cursor()
            cur1.execute(
                "SELECT firstName, Case when aveAll > ? and aveAll < ? THEN 'ast' Else 'beyn baze dade shode nist' END as 'uniExamNumbers' FROM students ",
                (addKoochak, addBozorg,))
            results = cur1.fetchall()
            filtered_results = [row for row in results if row[1] == 'ast']
            for row in filtered_results:
                print(row[0])

            cur1.close()
            conn1.close()

        PerintUserinputBetweenTwoNumber(addBozorg1, addkoochak1)
        main()
    elif getnumber == 9:
        def print_all():
            conn1 = sqlite3.connect("Students.db")

            cur1 = conn1.cursor()

            cur1.execute(
                "SELECT * FROM students ")
            # cur1.execute("SELECT firstName FROM students")
            # cur1.execute("SELECT lastName FROM students")
            # cur1.execute("SELECT uniNumber FROM students")
            # cur1.execute("SELECT firstName FROM students")
            # cur1.execute("SELECT firstName FROM students")
            # cur1.execute("SELECT firstName FROM students")
            # cur1.execute("SELECT firstName FROM students")
            # cur1.execute("SELECT firstName FROM students")
            # cur1.execute("SELECT firstName FROM students")
            # cur1.execute("SELECT firstName FROM students")
            # cur1.execute("SELECT firstName FROM students")
            # cur1.execute("SELECT firstName FROM students")
            # cur1.execute("SELECT firstName FROM students")
            row1 = cur1.fetchall()
            obj.print_db()
            formatted_rows = []
            for row in row1:
                formatted_row = f"student name = {row[0]} student last name =  {row[1]} student uni number = {row[2]} student normalNumber1 = {row[3]} student normalNumber2 = {row[4]} student normalNumber3 = {row[5]} student normalNumber4 {row[6]} student ormalNumber5 {row[7]} student spcificNumber1 {row[8]} student spcificNumber2{row[9]} student spcificNumber3{row[10]} student spcificNumber4{row[11]} student spcificNumber4 {row[12]} avarage normal numbers = {row[13]} avarage specific numbers = {row[14]} avarage all numbers {row[15]}               \n"
                formatted_rows.append(formatted_row)
            print("All students are : \n")
            for formatted_row in formatted_rows:
                print(formatted_row)

            cur1.close()
            conn1.close()
        print_all()
        main()
    elif getnumber == 10:
        obj.print_db()
        main()
    elif getnumber == 11:
        exit(0)
    elif getnumber == 12:
        database1.database1.delete()
    else:
        exitPrint = "exit"
        print("\n Number for operation not found ({})".format(exitPrint))
        exit(0)


# cursorForStudent.execute("SELECT * FROM students")

database1.database1.delete()
obj = database1.database1()
obj.createTable()
main()
