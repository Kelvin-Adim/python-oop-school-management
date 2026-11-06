# OOP Features in Python
# This program uses a school management system to demonstrate the four main features of OOP: Encapsulation, Inheritance, Polymorphism, and Abstraction.
from abc import ABC, abstractmethod

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def introduce(self):
        print(f"My name is {self.name} and I am {self.__age} years old.")
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Invalid Age.")

class SchoolActivity(ABC):
    @abstractmethod
    def activity(self):
        pass

class Student(Person, SchoolActivity):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
    def study(self):
        print(f"I am studying {self.course}.")
    def activity(self):
        print("I am attending lectures.")

class GraduateStudent(Student):
    def activity(self):
        print("I am conducting research")

graduate1 = GraduateStudent("Alya", 18, "Russian")
student1 = Student("Kelvin", 17, "Computer Science")
student1.introduce()
student1.study()

student1.set_age(18)
print(student1.get_age())
student1.activity()
graduate1.activity()