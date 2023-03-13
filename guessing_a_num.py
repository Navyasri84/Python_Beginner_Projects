import random

num = random.randint(1, 10)
name= input("What is your Name? ")
print(f"Okay {name}. I am guessing a number between 1 and 10.")
guess = None

while guess != num:
    guess = int(input("Now you can start guessing a number: "))

    if (guess == num):
        print("Congratulations! you won!")
        break

    elif (guess > num):
        print("Sorry. guess again!. Too high.")

    elif (guess < num):
        print("Sorry. guess again!. Too low.")
