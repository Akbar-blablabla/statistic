# def test_sequence():
#     num = 0
#     while num < 10:
#         yield num
#         num += 1
#
#
# for i in test_sequence():
#     print(i, end=".")
#
# print()
#
#
# def reverse_str(test_str):
#     length = len(test_str)
#     for i in range(length - 1, -1, -1):
#         yield test_str[i]
#
#
# for char in reverse_str("Wax30d"):
#     print(char, end=" ")


# def number_generator(n):
#     num = 1
#     while num <= n:
#         yield num
#         num += 1
#
# for i in number_generator(5):
#     print(i)
