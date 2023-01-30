
from random import randint
while True:
    username = input("\nEnter your name:")
    guess_number = float(input(f"Hello! {username} Now Enter Your Guessing Number Between 1 to 5:"))
    random_number = randint(1, 5)
    if guess_number == random_number:
        print(f"Congratulation {username} You Have Won This Number!! \n")
    else:
        print(f"Sorry {username} You are Loss This Number!!")
        print("Your Guessing Number are: ", random_number, "\n")

    next = input("Are You play Guess Number again? (Yes/No): \n")
    if next == "No":
        break
    if next == "Yes":
        continue
    else:
        break

