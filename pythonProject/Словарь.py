# Словарь = {"Словарь (dict) в Python представляет собой структуру данных,
# которая содержит коллекцию пар ключ-значение. Каждый ключ должен быть
# уникальным, а значение может быть любого типа данных. Словари являются
# изменяемыми и могут быть изменены, добавлены новые элементы или удалены существующие"}



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(thisdict)



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "year": 2020
# }
# print(thisdict)



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(len(thisdict))



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "colors": ["red", "white", "blue"]
# }



# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = thisdict["model"]



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = thisdict.get("model")



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = thisdict.keys()



# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = car.keys()
#
# print(x) #before the change
#
# car["color"] = "white"
#
# print(x) #after the change



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = thisdict.values()



# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
#
# x = car.values()
#
# print(x) #before the chenge
#
# car["year"] = 2020
#
# print(x) #after the change



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = thisdict.items()



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
#
# if "model" in thisdict:
#     print("Yes, 'model', is one of the keys in the thisdict dictionary")



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict.update({"year": 2020})



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict.popitem()
# print(thisdict)



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# del thisdict["model"]
# print(thisdict)



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict.clear()
# print(thisdict)



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for x in thisdict:
#     print(x)



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for x in thisdict:
#     print(thisdict[x])



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for x in thisdict.values():
#     print(x)



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for x in thisdict.keys():
#     print(x)



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for x, y in thisdict.items():
#     print(x, y)



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)



# myfamily = {
#     "child1"   : {
#         "name" : "Emil",
#         "year" : 2004
#     },
#     "child2"   : {
#         "name" : "Tobias",
#         "year" : 2007
#     },
#     "child3"   : {
#         "name" : "Linus",
#         "year" : 2011
#     }
# }



# child1 = {
#     "name" : "Emil",
#     "year" : 2004
#     }
# child2 = {
#     "name" : "Tobias",
#     "year" : 2007
#     }
# child3 = {
#     "name" : "Linus",
#     "year" : 2011
#     }
#
# myfamily = {
#     "child1" : child1,
#     "child2" : child2,
#     "child3" : child3
# }
#
# print(myfamily["child2"]["name"])



