from art import logo
import random
print(logo)

computer = random.randint(1, 100)
value = computer
print("Welcome to number guessing game, you'll be asked to choose numbers")

difficulty = input("Please Enter the difficulty h for hard e for easy ")

def result(user, computer):
    if int(user) < int(value):
        print("Too Low")
    elif int(user) > int(value):
        print("Too High")
    else:
        print("You guessed it correct")

if difficulty == "e":
    for count in range(9):
        user = input("Please enter a number between 1 to 100 ")
        print(value)
        value = computer
        result(user, value)
        value = None
if difficulty == "h":
    for count in range(4):
        user = input("Please enter a number between 1 to 100 ")
        print(value)
        value = computer
        result(user, value)
        value = None
