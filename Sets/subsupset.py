even = set(range(0, 40, 2))
print(sorted(even))

squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print(sorted(squares))

if squares.issubset(even):
    print("squares is subset of even")
if even.issuperset(squares):
    print("even is superset of squares")

