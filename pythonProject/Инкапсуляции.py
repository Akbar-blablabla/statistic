# Инкапсуляция = ("Инкапсуляция в Python - это механизм, который позволяет
# скрыть детали реализации объекта от внешнего мира и обеспечивает доступ
# к ним только через интерфейс класса. Это достигается путем объявления
# атрибутов или методов класса как закрытых (private) или защищенных (protected),
# что ограничивает доступ к ним извне. В Python инкапсуляция реализуется с помощью
# использования двойного подчеркивания перед именем атрибута или метода (например, __имя)")


# class Book:
#     def __init__(self, title, quantity, author, prince):
#         self.title = title
#         self.quantity = quantity
#         self.author = author
#         self.prince = prince
#         self.__discount = 0.10
#
#
#     def __repr__(self):
#         return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Prince: {self.prince}"
#
#
#
# book1 = Book('Book 1', 12, 'Author 1', 120)
#
#
# print(book1.title)
# print(book1.quantity)
# print(book1.author)
# print(book1.prince)
# print(book1.__discount)


# class Book:
#     def __init__(self, title, quantity, author, prince):
#         self.quantity = quantity
#         self.title = title
#         self.author = author
#         self.__prince = prince
#         self.__discount = None
#
#     def set_discount(self, discount):
#         self.__discount = discount
#
#     def get_prince(self):
#         if self.__discount:
#             return self.__prince * (1 - self.__discount)
#         return self.__prince
#
#     def __repr__(self):
#         return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Prince: {self.__prince}"
#
#
# single__book = Book('Two States', 1, 'Chetan Bhagan', 200)
#
# bulk_books = Book('Two States', 25, 'Chetan Bhagat', 200)
# bulk_books.set_discount(0.20)
#
# print(single__book.get_prince())
# print(bulk_books.get_prince())
# print(single__book)
# print(bulk_books)


# class Ckidochka:
#     def __init__(self, priceApple, priceCherry, priceCola):
#         self.priceApple = priceApple
#         self.priceCherry = priceCherry
#         self.priceCola = priceCola
#         self.__discount = None
#
#     def set_discount(self, discount):
#         self.__discount = discount
#
#     def get_priceApple(self):
#         return self.priceApple * (1 - self.__discount)
#
#     def __repr__(self):
#         return f"Price Apple: {self.priceApple}, Price Cherry: {self.priceCherry}, Price Cola: {self.priceCola}"
#
#
# print("Magazin Skidochka")
# aa = Ckidochka(20000, 60000, 13000)
# print("Cherry Price without discount: {}".format(aa.priceCherry))
# print("Apple Price without discount: {}".format(aa.priceApple))
# print("Cola Price without discount: {}".format(aa.priceCola))
# aa.set_discount(0.25)
# print()
# print("Apple with Discount: {}".format(aa.get_priceApple()))
# print()
#
# class Havas:
#     def __init__(self, priceApple, priceCherry, priceCola):
#         self.priceApple = priceApple
#         self.priceCherry = priceCherry
#         self.priceCola = priceCola
#         self.__discount = None
#
#     def set_discount(self, discount):
#         self.__discount = discount
#
#     def get_priceApple(self):
#         return self.priceApple * (1 - self.__discount)
#
#     def __repr__(self):
#         return f"Price Apple: {self.priceApple}, Price Cherry: {self.priceCherry}, Price Cola: {self.priceCola}"
#
# print()
# print("Magazin Havas")
# aa = Ckidochka(20000, 60000, 13000)
# print("Cherry Price without discount: {}".format(aa.priceCherry))
# print("Apple Price without discount: {}".format(aa.priceApple))
# print("Cola Price without discount: {}".format(aa.priceCola))
# aa.set_discount(0.35)
# print()
# print("Apple with Discount: {}".format(aa.get_priceApple()))
