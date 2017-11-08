import sqlite3

db_name = raw_input("Enter your database name:") + '.db'

conn = sqlite3.connect(db_name)
c = conn.cursor()

class Student (object):

    def __init__(self, firstName,middleInit, lastName, idNum, Course):
        self.fname=firstName
        self.mi=middleInit
        self.lname=lastName
        self.idnum=idNum
        self.course=Course


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS studentRecord(FirstName TEXT, MiddleInitial TEXT, LastName TEXT, ID TEXT, Course TEXT)')

def add_entry(student):
    c.execute("INSERT INTO studentRecord (FirstName, MiddleInitial, LastName, ID, Course) VALUES (?,?,?,?,?)",
        (student.fname,student.mi, student.lname,student.idnum,student.course))
    conn.commit()

def delete_entry():
    idno = raw_input("enter ID: ")
    c.execute("DELETE FROM studentRecord WHERE ID = ?", (idno,))
    conn.commit()

def search_entry():
    select = raw_input("Enter ID: ")
    c.execute("SELECT*FROM studentRecord where ID = ?", (select,))
    for row in c.fetchall():
        print "\nID number: ", row[3], "\nFirst Name: ", row[0], "\nMiddle Initial: ", row[1], "\nLast Name: ", row[2], "\nCourse: ", row[4]
    conn.commit()

def update_entry():
    select = raw_input("Enter ID: ")
    choice = raw_input("What to update? \n>>>FName\n>>>LName\n>>>MInitial\n>>>Course\n")
    if choice == "FName":
        change = raw_input("Enter new first name: ")
        conn.execute("UPDATE studentRecord set FirstName = ? where ID = ?", (change,select,))
        conn.commit()
    elif choice == "LName":
        change = raw_input("Enter new last name: ")
        conn.execute("UPDATE studentRecord set LastName = ? where ID = ?", (change,select,))
        conn.commit()
    elif choice == "MInitial":
        change = raw_input("Enter new middle initial: ")
        conn.execute("UPDATE studentRecord set MiddleInitial = ? where ID = ?", (change,select,))
        conn.commit()
    elif choice == "Course":
        change = raw_input("Enter new course: ")
        conn.execute("UPDATE studentRecord set Course = ? where ID = ?", (change,select,))
        conn.commit()

def sort_entry():
    choice = raw_input("Sort how?: \nLastName, ID, Course: \n")
    if choice == "LastName":
        c.execute("SELECT*FROM studentRecord ORDER BY LastName ASC")
        for row in c.fetchall():
            print row[0], row[1], row[2], row[3], row[4]
        conn.commit()
    if choice == "ID":
        c.execute("SELECT*FROM studentRecord ORDER BY ID ASC")
        for row in c.fetchall():
            print row[0], row[1], row[2], row[3], row[4]
        conn.commit()
    if choice == "Course":
        c.execute("SELECT*FROM studentRecord ORDER BY Course ASC")
        for row in c.fetchall():
            print row[0], row[1], row[2], row[3], row[4]
        conn.commit()


def main():
    create_table()
    while(True):

        choice1 = raw_input("ADD, DELETE, UPDATE, SORT, SEARCH: ")
        if choice1 == "ADD":
            f = raw_input("fn: ")
            m = raw_input("mi: ")
            l = raw_input("ln: ")
            i = raw_input("id: ")
            co = raw_input("c:")
            student = Student(f, m, l, i, co)
            add_entry(student)
        if choice1 == "DELETE":
            delete_entry()
        if choice1 == "SEARCH":
            search_entry()
        if choice1 == "UPDATE":
            update_entry()
        if choice1 == "SORT":
            sort_entry()

        choice2 = raw_input("EXIT? Y/N: ")
        if choice2 == "Y":
            break


    c.close()
    conn.close()


if __name__ == '__main__':
    main()
