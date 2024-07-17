# # Модификатор = ("Модификаторы в Python обычно используются для изменения поведения
# # классов и их членов. Они определяются ключевыми словами, такими как @staticmethod,
# # @classmethod, и @property. Каждый из них обеспечивает разные возможности:
# # @staticmethod позволяет определить метод, который не привязан к экземпляру класса,
# # @classmethod предоставляет доступ к методам класса, а @property создает метод,
# # который можно использовать как атрибут объекта")
#
#
# class Person:
#     def __init__(self, name, age):
#         self.personName = name
#         self.personAge = age
#
#     def displayAge(self):
#         print("Age:", self.personAge)
#
#
# obj = Person("R2J", 20)
#
# print("Name:", obj.personName)
#
# obj.displayAge()
#
# print()
#
#
# class Student:
#     _name = None
#     _roll = None
#     _branch = None
#
#     def __init__(self, name, roll, branch):
#         self._name = name
#         self._roll = roll
#         self._branch = branch
#
#     def _displayRollAndBranch(self):
#         print("Roll:", self._roll)
#         print("Branch:", self._branch)
#
#
# class Person(Student):
#     def __init__(self, name, roll, branch):
#         Student.__init__(self, name, roll, branch)
#
#     def displayDetails(self):
#         print("Name:", self._name)
#
#         self._displayRollAndBranch()
#
#
# obj = Person("R2J", 17062556, "Information Technology")
#
# obj.displayDetails()


# class Computer:
#
#     def __init__(self):
#         self.__maxprice = 900
#
#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))
#
#     def setMexPrice(self, price):
#         self.__maxprice = price
#
#
# c = Computer()
# c.sell()
#
# c.__maxprice = 1000
# c.sell()
#
# c.setMexPrice(1000)
# c.sell()
