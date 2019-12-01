# i =0
# while i < 10:
#     print("i is {}".format(i))
#     i += 1

available_exits = ["north", "south east", "west"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit=input("please enter destination")
    if chosen_exit == "quit":
        print("game over")
        break
else:
    print("aren't you glad you are out of there")


