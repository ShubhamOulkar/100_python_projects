import random
from higherlower_art import logo, vs
from higherlower_game_data import data
print(logo)
a = random.randint(0, 49)  # list of 50 dictionary
b = random.randint(0, 49)

ans = 0  # counting score for correct guess
choice = "True"   # Flag for while loop
while choice == "True":
    if a == b:
        b = random.randint(0, 49)

    print(f"\n Compare A -> Name: {data[a]['name']}, {data[a]['description']}, {data[a]['country']}")
    print(vs)
    print(f"\n Against b -> Name: {data[b]['name']}, {data[b]['description']}, {data[b]['country']}")

    insta_a = data[a]['follower_count']
    insta_b = data[b]['follower_count']

    guess = input("\nWho has more followers? Choose A or B : ").lower()

    if insta_a > insta_b and guess == 'a':
        a = a  # swaping variables
        b = random.randint(0, 49)
        ans += 1  # counting score for correct guess
    elif insta_a < insta_b and guess == 'b':
        a = b  # swaping variables
        b = random.randint(0, 49)
        ans += 1  # counting score for correct guess
    else:
        choice = "False"  # exit flag for while loop
        print(f"Sorry thats wrong, Your score is {ans}.")
