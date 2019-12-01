parrot = "green parrot"

letter = input("enter a character")
if letter in parrot:
    print("give me {} character".format(letter))

else:
    print("i don't need that letter")