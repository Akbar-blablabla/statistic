# Кортеж = ("Кортеж (tuple) в Python - это упорядоченная и неизменяемая коллекция элементов.
# Он похож на список, но не может быть изменен после создания.
# Кортежи создаются с использованием круглых скобок или функции 'tuple()',
# их элементы разделяются запятыми. Кортежи часто используются для представления неизменяемых наборов данных,
# ключей словаря или возвращаемых значений функций")



# thistuple = ("aplle", "banana", "cherry")
# print(thistuple)



# thistuple = ("aplle", "banana", "cherry", "apple", "cherry")
# print(thistuple)



# thistuple = ("aplle", "banana", "cherry")
# print(len(thistuple))



# thistuple = ("aplle",)
# print(type(thistuple))
#
# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))



# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)



# tuple1 = ("abc", 34, True, 40, "male")



# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
#
# print(x)



# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)



# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
#
# print(thistuple)



# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)



# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists



# fruits = ("apple", "banana", "cherry")
#
# (green, yellow, red,) = fruits
#
# print(green)
# print(yellow)
# print(red)



# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
# (green, yellow, *red,) = fruits
#
# print(green)
# print(yellow)
# print(red)



# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
#
# (green, *tropic, red,) = fruits
#
# print(green)
# print(tropic)
# print(red)



# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#     print(x)



# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#     print(thistuple[i])



# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i =i + 1



