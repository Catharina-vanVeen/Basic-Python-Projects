

class Person:
    fname = ""
    lname = ""
    dob = ""
    address = ""

    def __init__(self, fname, lname, dob, address):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.address = address

    def getName(self):
        return "{} {}".format(self.fname, self.lname)

    def getInfo(self):
        msg = "\nName:\t\t{} {}\nAddress:\t{}\nDate of birth:\t{}".format(self.fname, self.lname, self.address, self.dob)
        return msg


class Student(Person):
    parent = ""
    grade = 0

    def __init__(self, fname, lname, dob, address, parent, grade):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.address = address
        self.parent = parent
        self.grade = grade

    def getInfo(self):
        msg = "\nName:\t\t{} {}\nAddress:\t{}\nDate of birth:\t{}\nGrade:\t\t{}\nParent:\t\t{}".format(self.fname, self.lname, self.address, self.dob, self.grade, self.parent)
        return msg

    def getGrade(self):
        return self.grade

        
class Teacher(Person):
    subjects = []
    payGrade = 0

    def __init__(self, fname, lname, dob, address, subjects, paygrade):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.address = address
        self.subjects = subjects
        self.paygrade = paygrade

    def getInfo(self):
        msg = "\nName:\t\t{} {}\nAddress:\t{}\nDate of birth:\t{}\nSubjects:\t{}\nPaygrade:\t{}".format(self.fname, self.lname, self.address, self.dob, self.subjects, self.paygrade)
        return msg


if __name__ == "__main__":
    student1 = Student("Maria", "van Veen", "01/01/2014", "123 Main Street", "Mom van Veen", 6)
    print(student1.getInfo())    
    teacher1 = Teacher("Karin", "Dawson", "01/01/1970", "11 North Street", ["english", "math"], 2)
    print(teacher1.getInfo())
    person1 = Person("Catharina", "van Veen", "01/01/1980", "30 South Street")
    print(person1.getInfo())
    print()
    print(student1.getName())
    print(student1.getGrade())
