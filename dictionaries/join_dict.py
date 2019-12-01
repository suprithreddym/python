locations = {0: "you are sitting in front of computer learning python",
             1: "you are sitting at the end of the road before a small brick building",
             2: "you are at the top of the hill",
             3: "you are inside a building",
             4: "you are in the valley behind a stream",
             5: "you are in the forest"}
exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc =1
while True:
    availableexits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction = input("available exits are " + availableexits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
        print(loc)
    else:
        print("You cannot go in that direction")