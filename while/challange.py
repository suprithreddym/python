import random
highest = 1000
answer = random.randint(1, highest)
print("please give a number between 1 and {}".format(highest))
guess = int(input())
while guess != answer:
    if 1 <= guess < 1000:
        if guess > answer:
            print("please enter lower value")
        else:
            print("please enter higher value")
        guess = int(input())
    elif guess == 0:
        break
    else:
        print("please enter value between 1 and 1000")
        guess = int(input())
else:
    print("you guessed correctly")
