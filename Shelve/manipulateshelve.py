import shelve

#with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('shelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "a good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

    # print(fruit["lemon"])
    # print(fruit["grape"])
    #
    # fruit["lime"] = "great with tequila"
    # for snack in fruit:
    #     print(snack + ":" + fruit[snack])

# while True:
#     shelf_key = input("Please enter the key:")
#     if shelf_key == "quit":
#         break
#
#     description = fruit.get(shelf_key, "we don't have a " + shelf_key)
#     print(description)

while True:
    shelf_key = input("please enter the key")
    if shelf_key == "quit":
        break
    if shelf_key in fruit:
        description = fruit[shelf_key]
        print(description)
    else:
        print("we don't have a " + shelf_key)

fruit.close()
