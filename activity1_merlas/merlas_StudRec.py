from Tkinter import *
import fileinput

root = Tk()
root.title("StudentRec")
root.grid()
root.geometry("300x500")
root.resizable(width=False, height=False)
files = StringVar()
label = Label(root, text="Student Record", bg = "lightgreen", font = "fixedsys 20 bold").pack()
label2 = Label(root, text ="Enter file name:").pack()
fileInput = Entry(root, textvariable=files, relief=GROOVE, bg="lightgreen").pack()

def openFile():
    def addWindow():
        def addData():
            i = str(idno.get())
            s = str(names.get())
            c = str(courses.get())
            #student = Student(i, n, c)
            dbfile= open(str(files.get()), 'a+')
            dbfile.write(i + " " + s + " " + c + '\n')
            dbfile.close()
            nameEntry.delete(0,"end")
            idEntry.delete(0,"end")
            courseEntry.delete(0,"end")

        newWin = Toplevel()
        newWin.geometry("200x100")
        newWin.resizable(width=False, height=False)
        newWin.title("ADD")

        add_id = Label(newWin, text="ID no.").grid(row=0, column=0)
        idno = StringVar(None)
        idEntry = Entry(newWin, textvariable=idno,bg="lightgreen")
        idEntry.grid(row=0, column=1)
        add_name = Label(newWin, text="Name").grid(row=1, column=0)
        names = StringVar(None)
        nameEntry = Entry(newWin, textvariable=names,bg="lightgreen")
        nameEntry.grid(row=1, column=1)
        add_course = Label(newWin, text="Course").grid(row=2, column=0)
        courses = StringVar(None)
        courseEntry = Entry(newWin, textvariable=courses, bg="lightgreen")
        courseEntry.grid(row=2, column=1)

        addFinal = Button(newWin, text="ADD", command=addData, relief=GROOVE).grid(row=4, column=1)

    def deleteWindow():
        def deleteData():
            getID = str(idno.get())
            fileGet = str(files.get())
            dbfile = open(fileGet)
            newLine = []
            for line in dbfile:
                currentLine = line.split()
                if not getID == currentLine[0]:
                    newLine.append(line)
            dbfile.close()
            dbfile = open(fileGet, 'w+')
            dbfile.writelines(newLine)
            dbfile.close()
            idEntry.delete(0,"end")
            msg = Label(deleteWin, text="Removed Successfully", font="fixedsys 12 bold").place(x=10,y=50)

        deleteWin = Toplevel()
        deleteWin.geometry("200x100")
        deleteWin.resizable(width=False, height=False)
        deleteWin.title("DELETE")
        delete_id = Label(deleteWin, text="ID no. ").grid(row=0,column=0)
        idno = StringVar(None)
        idEntry = Entry(deleteWin, text=idno, bg="lightgreen")
        idEntry.grid(row=0,column=1)
        deleteFinal = Button(deleteWin, text="REMOVE", command=deleteData, relief=GROOVE).grid(row=4, column=1)

    def updateWindow():
        def updateData():
            def updateIn():
                newNo = str(idno.get())+' '
                newName = str(names.get())+' '
                newCourse = str(courses.get())+' '
                newData = newNo+newName+newCourse
                fileGet = str(files.get())
                matchID = str(enterID.get())

                for line in fileinput.FileInput(fileGet, inplace=1):
                    if matchID in line:
                        line = line.replace(line, newData)
                    print line
                newid.delete(0, "end")
                newname.delete(0, "end")
                newcourse.delete(0, "end")

            matchingID = str(enterID.get())
            fop = str(files.get())
            fileRead = open(fop, 'r')
            for line in fileRead:
                currentLine = line.split()
                if currentLine[0] == matchingID:
                    displayLine = Label(updateWin, text="Current record: \n"+line, font="fixedsys 7 bold" ).place(x=10,y=85)
                    new_id = Label(updateWin, text="ID no.").place(x=10, y=150)
                    idno = StringVar(None)
                    newid = Entry(updateWin, textvariable=idno, bg="lightgreen")
                    newid.place(x=55, y=150)
                    new_name = Label(updateWin, text="Name").place(x=10, y=175)
                    names = StringVar(None)
                    newname = Entry(updateWin, textvariable=names, bg="lightgreen")
                    newname.place(x=55, y=175)
                    new_course = Label(updateWin, text="Course").place(x=10, y=200)
                    courses = StringVar(None)
                    newcourse = Entry(updateWin, textvariable=courses, bg="lightgreen")
                    newcourse.place(x=55, y=200)
                    addFinal = Button(updateWin, text="CHANGE", command=updateIn, relief=GROOVE).place(x=100, y=250)
            fileRead.close()
            IDstore.delete(0, "end")
        updateWin = Toplevel()
        updateWin.geometry("200x300")
        updateWin.resizable(width=False, height=False)
        updateWin.title("UPDATE")

        searchID = Label(updateWin, text="ID no.").place(x=10, y=40)
        enterID = StringVar(None)
        IDstore = Entry(updateWin, textvariable=enterID, bg="lightgreen")
        IDstore.place(x=55, y=40)
        searchButt = Button(updateWin,text="Search", width=12, height=1, command = updateData).place(x=70, y=60)


    filename = str(files.get())

    nfile = open(filename, 'a+')
    display = Label(root, text="Opened file successfully", font = "fixedsys 12 bold").place(x=10,y=120)
    display2 = Label(root, text="*to update listbox, open file again", font="times 8 italic").place(x=10, y=145)
    studentList = Listbox(root, width=45, height=14, bg="lightgreen")

    for line in nfile:
        studentList.insert(END, line)
    studentList.place(x=12, y=230)
    nfile.close()

    addStud = Button(root, text="Add Student", width = 12, height = 2, command=addWindow, relief=GROOVE).place(x=12,y=170)
    deleteStud = Button(root, text="Remove Student", width = 12, height = 2,command=deleteWindow, relief=GROOVE).place(x=115,y=170)
    updateStud = Button(root, text="Update", width = 9, height = 2,command=updateWindow, relief=GROOVE).place(x=215, y=170)

addFile = Button(root, text="Open File", width = 12, height = 2, command=openFile, relief=GROOVE).pack()
root.mainloop()
