print("please enter number between 1 and 10")
guess = int(input())
if guess !=5:
    if guess < 5:
        print("please enter higher value")
    else:
        print("please enter lower value")
    guess = int(input())
    if guess == 5:
        print("you guessed correctly")
    else:
        print("sorry you have not quessed correctly")
else:
    print("you guessed correctly")