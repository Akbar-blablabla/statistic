# Итераторы = ("Итераторы в Python - это объекты, которые позволяют поочередно перебирать
# элементы коллекции или последовательности данных. Они реализуют протокол итерации,который
# включает методы __iter__() для инициализации итератора и __next__() для получения следующего элемента")


# class Example_range:
#     def __init__(self, n):
#         self.i = 4
#         self.n = n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i < self.n:
#             i = self.i
#             self.i += 1
#             return i
#         else:
#             raise StopIteration()
#
#
# n = Example_range(15)
# print(list(n))
#
# n = Example_range(15)
# for i in n:
#     print(i, end=',')
#
# print()
#
# n = Example_range(15)
# iterator = iter(n)
# while True:
#     try:
#         x = iterator.__next__()
#         print(x, end=',')
#     except StopIteration as e:
#         break


# class Counter:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.limit:
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.current
#
#
# counter = Counter(5)
#
# for num in counter:
#     print(num)
