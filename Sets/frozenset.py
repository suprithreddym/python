even = frozenset(range(0, 100, 2))
print(even)

even.add(5) # gives error as frozen set is immutable