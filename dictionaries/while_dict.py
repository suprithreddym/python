fruit = {"1": "suprith",
        "2":"sunitha",
        "3":"sunny",
        "4":"siva",
        "5":"soumya"}

print(fruit)
while True:
    dict_key = input("please enter a fruit:")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key, "we don't have a " + dict_key)
    print(description)
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("we dont have a " + dict_key)

