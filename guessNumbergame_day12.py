import random
from GuessGame_art import logo

rn = random.randint(1,100)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "easy":
    diff = 11
else:
    diff = 6

def guess_game(diff):
    a = 1
    while a < diff:
        gn = int(input("Guess a number: "))
        if gn != rn:
            print(f"You have {diff - 1 - a} attempts remaining to guess the number.")
        a += 1
        if rn > gn:
            print("Guess is TOO SMALL")
        elif rn < gn:
            print("Guess is TOO LARGE")
        else:
            a = 12
            print("Perfect Guess, you win !")
        if a == diff and gn != rn:
            print("Your attempts are exhausted. \nYou lose ! ")

if level == "easy" or level == "hard":
    guess_game(diff)
else:
    print("Please put valid input.")

    