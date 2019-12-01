fruit = {"orange": "suprith , is, good, boy",
         "apple":"sunitha, is , good, mother",
         "grape":"sunny, is, good, brother",
         "lemon":"siva,  is , good , father",
         "lime":"soumya, is good sister"}

print(fruit)
for snack in fruit:
    print(snack + " " +fruit[snack])

# sorting above one
print('-' * 40)
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
ordered_keys = sorted(list(fruit.keys()))
for f in ordered_keys:
    print(f + " " + fruit[f])

print('-' * 40)

for f in sorted(fruit.keys()):
    print(f + " " + fruit[f])

print('-' * 40)

for val in fruit.values():
    print(val)
print('-' * 40)

for val in fruit:
    print(fruit[val])

print(fruit.keys())

print(fruit.values())
