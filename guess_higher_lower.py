import random
from higherlower_art import logo, vs
from higherlower_game_data import data

a = random.randint(0, 49)
b = random.randint(0, 49)
ans = 0
choice = "True"
while choice == "True":
    print(f"\n (A) Name: {data[a]['name']}\n Description: {data[a]['description']}\n Country: {data[a]['country']}")
    print(vs)
    print(f"\n (B) Name: {data[b]['name']}\n Description: {data[b]['description']}\n Country: {data[b]['country']}")

    insta_a = data[a]['follower_count']
    insta_b = data[b]['follower_count']

    guess = input("\nChoose A or B : ").lower()

    if insta_a > insta_b and guess == 'a':
        a = a
        b = random.randint(0, 49)
        ans += 1
    elif insta_a < insta_b and guess == 'b':
        a = b
        b = random.randint(0, 49)
        ans += 1
    else:
        choice = "False"
        print(f"Your score is {ans}.")



