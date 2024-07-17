# Декораторы = ("Декораторы в Python представляют собой особый вид функций,
# которые позволяют изменять поведение других функций или методов
# без изменения их собственного кода. Они используются для добавления
# функциональности к существующим функциям, обертывая их вокруг других функций.
# Основные черты декораторов: Синтаксис - Декораторы представляют собой функции,
# которые принимают функцию в качестве аргумента и возвращают другую функцию")


# def test_decorator(func):
#     def function_wrapper(x):
#         print("Before calling " +func.__name__)
#         res = func(x)
#         print(res)
#         print("After calling " + func.__name__)
#
#     return function_wrapper
#
#
# @test_decorator
# def sqr(n):
#     return n ** 2
#
#
# sqr(7)

# def lowercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_lowercase = func.lower()
#         return make_lowercase
#
#     return wrapper
#
#
# def split_string(function):
#     def wrapper():
#         func = function()
#         splitString = func.split()
#         return splitString
#
#     return wrapper
#
#
# @split_string
# @lowercase_decorator
# def test_func():
#     return 'Hello OOP python'
#
#
# print(test_func())
