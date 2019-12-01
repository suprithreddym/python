fruit = {"orange": "suprith , is, good, boy",
         "apple":"sunitha, is , good, mother",
         "grape":"sunny, is, good, brother",
         "lemon":"siva,  is , good , father",
         "lime":"soumya, is good sister"}

print(fruit)

print(fruit.items())

t_tuple = tuple(fruit.items())  # converting dict to tuple
print(t_tuple)

for value in t_tuple:
    item, description = value
    print(item + " is " + description)

print(dict(t_tuple)) # converting tuple to dict
