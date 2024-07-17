# # Наследование = ("Наследование в Python позволяет классам наследовать
# # свойства и методы других классов. Один класс может наследовать от
# # одного или нескольких других классов. Дочерний класс (или подкласс)
# # наследует атрибуты и методы родительского класса (или суперкласса),
# # что позволяет повторно использовать код и создавать иерархии классов")

#
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
#
# # Use the Person class to create an object, and then execute the printname method:
#
# x = Person("John", "Doe")
# x.printname()
#
#
# class Student(Person):
#     pass


# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year
#
#
# x1 = Student("Shaxzod", "Sobitov", 2019)
#
# print(x1.lastname)
# print(x1.firstname)
# print(x1.graduationyear)


# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduation = year
#
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduation)
#
#
# ak1 = Student('Akbar', "Kurbanbayev", '2026')
# print(ak1.firstname)
# print(ak1.lastname)
# print(ak1.graduation)
# ak1.welcome()


# class Person(object):
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
#
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
#
#
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#
#
#
#
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
#
# # Use the Person class to create an object, and then execute the printname method:
#
# x = Person("John", "Doe")
#
# print(x.lastname)
# print(x.firstname)
# print(x.graduationyear)


# class Person(object):
#
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
#
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
#
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber:{}".format(self.idnumber))
#
#
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
#
#         # invoking the __init__ of the parent class
#         Person.__init__(self, name, idnumber)
#
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber:{}".format(self.idnumber))
#         print("Post:{}".format(self.post))
#
#     # creation of an object variable or an instance
#
#
# a = Employee("Shaxzod", 6970, 600, "Intern")
#
# # calling a function of the class Person using
# # its instance
# a.display()
# a.details()
#
# print(a.post)
