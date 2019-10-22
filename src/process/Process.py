from src.student.Students import NewStudent

class Processstudents(NewStudent):

    @staticmethod
    def addStudent():
        name = input("Enter the student name:")
        data = NewStudent(name)
        return data

    def studentMark(student, mark):
        student.marks.append(mark)


class Average(NewStudent):
    def calculateAverageMark(self):
        count = len(self.marks)
        if count == 0:
            return 0
        else:
            total_mark = sum(self.marks)
            return total_mark/count


    def display(student):
        print("{}, Average Mark: {}.".format(student.name, Average.calculateAverageMark(student)), "\n--------")


    def display_all_student(students):
        #enumerate method is used to get value and index of a dictonary
        for i, student in enumerate(students):
            print("ID:{}".format(i))
            Average.display(student)
