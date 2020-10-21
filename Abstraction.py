from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self):
        self.__name = ""
        
    def getName(self):
        return self.__name
        
    def setName(self, name):
        self.__name = name

    @abstractmethod
    def greeting(self):
        pass


class Teacher(Person):

    def greeting(self):
        print("My name is {}. I am a teacher".format(self.getName()))

class Student(Person):

    def greeting(self):
        print("My name is {}. I am a student".format(self.getName()))


t1 = Teacher()
t1.setName("John Doe")

s1 = Student()
s1.setName("Mary Smith")

t1.greeting()
s1.greeting()
