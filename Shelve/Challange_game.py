import shelve

locations = shelve.open("locations")
vocabulary = shelve.open("vocabulary")
loc = '1'
while True:
    availableexits = ", ".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])

    if loc == '0':
        break
    else:
        allexits = locations[loc]["exits"].copy()
        allexits.update(locations[loc]["namedexits"])

    direction = input("available exits are " + availableexits).upper()
    print()
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in allexits:
        loc = allexits[direction]
    else:
        print("You cannot go in that direction")