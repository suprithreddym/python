locations = {0:{"desc": "you are sitting in front of computer learning python",
                "exits": {},
                "namedexits": {}},
             1: {"desc":"you are sitting at the end of the road before a small brick building",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedexits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc":"you are at the top of the hill",
                 "exits":{"N": 5, "Q": 0},
                 "namedexits":{"5": 5}},
             3: {"desc": "you are inside a building",
                 "exits": {"W": 1, "Q": 0},
                 "namedexits": {"1":1}},
             4: {"desc":"you are in the valley behind a stream",
                 "exits":{"N": 1, "W": 2, "Q": 0},
                 "namedexits": {"1": 1, "2": 2}},
             5: {"desc":"you are in the forest",
                 "exits":{"W": 2, "S": 1, "Q": 0},
                 "namedexits": {"2": 2, "1": 1}}
                }

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING":"3",
              "VALLEY":"4",
              "FOREST":"5"}

loc = 1
while True:
    availableexits = ", ".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])

    if loc == 0:
        break
    else:
        allexits = locations[loc]["exits"].copy()
        allexits.update(locations[loc]["namedexits"])

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

    if direction in allexits:
        loc = allexits[direction]
    else:
        print("You cannot go in that direction")