# Полиморфимзм = ("Полиморфизм в Python - это способность объектов разных
# типов обрабатывать одни и те же операции. Это позволяет использовать один
# и тот же метод для различных типов данных, что делает код более гибким и универсальным")


# class Bird:
#
#     def intro(self):
#         print("There are many types of birds.")
#
#     def flight(self):
#         print("Most of the birds can fly but some cannot.")
#
#
# class sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly.")
#
#
# class ostrich(Bird):
#
#     def flight(self):
#         print("Ostrich cannot fly")
#
#
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()
#
# obj_bird.flight()
#
# obj_spr.flight()
#
# obj_ost.flight()


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def move(self):
#         print("Drive!")
#
# class Boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def move(self):
#         print("Sail!")
#
# class Plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Fly!")
#
#
# car1 = Car("Ford", "Mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = Plane("Boeing", "747")
#
# for x in (car1, boat1, plane1):
#     x.move()


# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def move(self):
#         print("Move!")
#
#
# class Car(Vehicle):
#     pass
#
#
# class Boat(Vehicle):
#     def move(self):
#         print("Sail!")
#
#
# class Plane(Vehicle):
#     def move(self):
#         print("Fly!")
#
#
# car1 = Car("Ford", "Mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = Plane("Boeing", "747")
#
# for x in (car1, boat1, plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()

# obj = Car("Nexia", 'GM')
# print(obj.brand)
# print(obj.model)
#
# obj.move()
