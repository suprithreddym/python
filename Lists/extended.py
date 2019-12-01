# list_1 = []
# list_2 = list()
# print("list 1: {}".format(list_1))
# print("list 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("lists are equal")
#
# print(list("the lists are equal"))

#=================================

# even = [2, 4, 6, 8]
# another_even = list(even)
#
# print(another_even == even)
# print(another_even is even)
#
# another_even.sort(reverse=True)
# print(even)
#
# another_even = even
# another_even.sort(reverse=True)
# print(even)

#================================

even = [2, 4, 6, 8]
another_even = sorted(even, reverse=True)
print(another_even == even)


