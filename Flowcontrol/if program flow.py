# name = input("please enter your name")
# age=int(input("how old are you {0}?").format(name))
# print(name + " is " + str(age))
#
# if age >= 18:
#     print("you are eligible to vote")
# else:
#     print("please come back in {0}".format(18-age))
print("please guess a number between 1 and 10")
guess = int(input())
if guess < 5:
    print("please guess higher")
    guess = int(input())
    if guess == 5:
        print("you guessed correctly")
    else:
        print("sorry you have not guesses correctly")
elif guess > 5:
    print("please guess lower")
    guess = int(input())
    if guess == 5:
        print("guessed correctly")
    else:
        print("sorry you have not guesses correctly")
else:
    print("you got it first time")