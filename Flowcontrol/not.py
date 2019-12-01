parrot = "green parrot"

letter = input("enter a character")
if letter not in parrot:
    print("i don't need that letter")

else:
    print("give me {} character".format(letter))
