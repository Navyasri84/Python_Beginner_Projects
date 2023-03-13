import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = int(input("guess a number between 1 and 10: "))

    if (guess == num):
        print("Congratulations! you won!")
        break

    elif (guess > num):
        print("Sorry. guess again!. Too high.")

    elif (guess < num):
        print("Sorry. guess again!. Too low.")