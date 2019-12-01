even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

print(even.union(squares))    # union
print(len(even.union(squares)))

print("-" * 40)

print(even.intersection(squares))   # intersection
print(even & squares)
print(squares.intersection(even))
print(squares & even)

