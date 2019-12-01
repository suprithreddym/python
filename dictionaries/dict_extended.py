fruit = {"orange": "suprith , is, good, boy",
         "apple":"sunitha, is , good, mother",
         "grape":"sunny, is, good, brother",
         "lemon":"siva,  is , good , father",
         "lime":"soumya, is good sister"}
print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmm, lovely",
       "spinach": "can i have some more fruit please"}

print(veg)

veg.update(fruit) # update command

print(veg)

print(fruit.update(veg))
print(fruit)

nice_and_tasty = fruit.copy() # copy command
nice_and_tasty.update(veg)
print(nice_and_tasty)
