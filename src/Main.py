from src.process.Process import Average
from src.process.Process import Processstudents


studentlist = []


if __name__=="__main__":

    average = Average
    processstudents=Processstudents

    options=input("Enter 'p' to display all students\n"
                  "Enter 'a' to add a new student\n"
                  "Enter 'm' to add a new mark\n"
                  "or Enter 'q' to quit \n"
                  "=======================\n")
    while options != "q":
        if options == "p":
            average.display_all_student(studentlist)
        elif options == "a":
            studentlist.append(processstudents.addStudent())
        elif options == "m":
            studentid = int(input("Enter the student id:\n"))
            student = studentlist[studentid]
            newstudentmark = int(input("Enter the student mark:\n"))
            processstudents.studentMark(student, newstudentmark)

        options = input("Enter 'p' to display all students\n"
                        "Enter 'a' to add a new student\n"
                        "Enter 'm' to add a new mark\n"
                        "or Enter 'q' to quit \n"
                        "=======================\n")
