# class Магазин:
#     def __init__(self, овощи, фрукты, напитки):
#         self.овощи = овощи
#         self.фрукты = фрукты
#         self.напитки = напитки
#
# a = Магазин("200kg", "260kg", "180l")
#
# print("Магазин")
# print(a.напитки, a.овощи, a.фрукты)
# print()
#
#
# class Рынок(Магазин):
#     def __init__(self, овощи, фрукты, напитки, сладости):
#         super().__init__(овощи, фрукты, напитки)
#         self.сладости = сладости
#
# b = Рынок("200kg", "210kg", "140l", "40crates")
#
# print("Рынок")
# print(b.напитки, b.овощи, b.фрукты, b.сладости)


# class Animal:
#     def speak(self):
#         pass
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
#
# def make_animal_speak(animal):
#     print(animal.speak())
#
#
# dog = Dog()
# cat = Cat()
#
# make_animal_speak(dog)
# make_animal_speak(cat)


# class Car:
#     def __init__(self, make, model, year):
#         self.__make = make
#         self.__model = model
#         self.__year = year
#
#     def get_make(self):
#         return self.__make
#
#     def set_make(self, make):
#         self.__make = make
#
#     def get_model(self):
#         return self.__model
#
#     def set_model(self, model):
#         self.__model = model
#
#     def get_year(self):
#         return self.__year
#
#     def set_year(self, year):
#         self.__year = year
#
#
# my_car = Car("Toyota", "Corolla", 2020)
#
#
# print(my_car.get_make())
# print(my_car.get_model())
# print(my_car.get_year())
# print()
#
# my_car.set_make("Honda")
# my_car.set_model("Civic")
# my_car.set_year(2022)
#
# print(my_car.get_make())
# print(my_car.get_model())
# print(my_car.get_year())
