even = set(range(0, 40, 2))
print(sorted(even))

squares_tuple = (4, 6, 9, 16,25)
squares = set(squares_tuple)
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(sorted(squares.difference(even)))
print(sorted(squares - even))


print("=" * 40)

print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))
