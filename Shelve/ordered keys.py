import shelve

#with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('shelfTest')
ordered_keys = list(fruit.keys())
ordered_keys.sort()

for f in ordered_keys:
    print(f + '-' + fruit[f])

# for v in fruit.values():
#     print(v)
# print(fruit.values())
#
# for u in fruit.items():
#     print(u)
# print(fruit.items())


fruit.close()

# difference between shelve and dictionary is shelf only accept strings as keys whereas dict accepts any keys