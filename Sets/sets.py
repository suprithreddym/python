farm_animals = {"sheep", "cow", "hen"} #sets
print(farm_animals)

for animal in farm_animals:
    print(animal)

wild_animals = set(["Tiger", "lion", "panther", "elephant", "hare"]) # passing lists to the set
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

empty_set = set()
empty_set_2 = {}
empty_set.add("a")
print(empty_set)
# empty_set_2.add("a") # gives error we need to use set constructure to add to empty set.
# print(empty_set_2)

even = set(range(0, 40, 2))
print(even)
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)