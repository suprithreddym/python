# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index('e'))
# print(my_string[4])
#
# small_decimals = range(0, 10)
# print(small_decimals)
#
# print(small_decimals.index(4))
#
# odd = range(1, 100000, 2)
#
# print(odd.index(987))
# print(odd[985])
#
# sevens = range(7, 1000000, 7)
# x=int(input("please enter positive value less than millions"))
# if x in sevens:
#     print("{} is divisible by seven".format(x))
#
# print(small_decimals)
# my_range = small_decimals[::4]
# print(my_range)
# print(my_range.index(4))

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)
for i in my_range:
    print(i)

print('=' * 40)

for i in range(3, 40, 3):
    print(i)

print(my_range == range(3, 40, 3))





