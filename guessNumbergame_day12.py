import random

rn = random.randint(1,100)

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
        a += 1
        if rn > gn:
            print("Guess is TOO SMALL.\nGuess Again.")
        elif rn < gn:
            print("Guess is TOO LARGE.\nGuess Again.")
        else:
            a = 12
            print(f"{gn} is Perfect Guess, you win ! ")
        if gn != rn:
            print(f"You have {diff - a} attempts remaining to guess the number.")
        if a == diff and gn != rn:
            print(f"Your attempts are exhausted.\nYou lose !\nNumber was {rn}. ")

if level == "easy" or level == "hard":
    guess_game(diff)
else:
    print("Please put valid input.")

    