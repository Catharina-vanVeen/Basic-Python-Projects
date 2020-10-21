

class Student:
    def __init__(self):
        self.__fname = ""
        self.__lname = ""
        self._address = ""

    def getName(self):
        return "{} {}".format(self.__fname, self.__lname)

    def setName(self, fname, lname):
        self.__fname = fname
        self.__lname = lname


stud1 = Student()
stud1.setName("John", "Doe")
print(stud1.getName())

# The following works with or without the underscore
stud1.address = "123 Main street"
print(stud1.address)

stud1._address = "123 West street"
print(stud1._address)

# does not get executed, but also no error message is shown
stud1.__fname = "karin" 
print(stud1.getName())

stud1.fname = "Jane" 
print(stud1.getName())
