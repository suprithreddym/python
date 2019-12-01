even = set(range(0, 40, 2))
print(sorted(even))

squares_tuple = (4, 6, 9, 16,25)
squares = set(squares_tuple)
print(sorted(squares))

print("symetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print("symetric squares minus even")
print(sorted(squares.symmetric_difference(even)))

squares.discard(6)
squares.remove(16)
squares.discard(8) # no error, discard
print(squares)
#squares.remove(8) # gives error