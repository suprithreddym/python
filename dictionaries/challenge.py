locations = {0: "you are sitting in front of computer learning python",
             1: "you are sitting at the end of the road before a small brick building",
             2: "you are at the top of the hill",
             3: "you are inside a building",
             4: "you are in the valley behind a stream",
             5: "you are in the forest"}
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = {"QUIT": "Q",
               "NORTH": "N",
               "SOUTH": "S",
               "EAST": "E",
               "WEST": "W"}

loc =1
while True:
    availableexits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction = input("available exits are " + availableexits).upper()
    print()
    if len(direction) > 1:
        # for word in volcabulary:
        #     print(word)
        #     if word in direction:
        #         direction = volcabulary[word]
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]
        print(loc)
    else:
        print("You cannot go in that direction")