import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ga():
    cards = [random.randint(1, 11), random.randint(1, 11)]
    gambler = [random.randint(1, 11)]
    print(f"Your cards {cards}")
    print(f"Dealer card {gambler}")
    extra = input("Do you want extra card? y/n")
    if extra == "y":
        cards.append(random.randint(1,11))
        c = sum(cards)
        gambler.append(random.randint(1,11))
        g = sum(gambler)
        if c > 21 :
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler},\n Dealer Win!")
        elif c > g :
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler} ,\n You Win!")
        elif c < g :
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler}, \n Dealer Win!")
    else:
        c = sum(cards)
        gambler.append(random.randint(1,11))
        g = sum(gambler)
        if c > 21 :
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler},\n Dealer Win!")
        elif c > g :
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler},\n You Win!")
        elif c < g :
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler}, \n Dealer Win!")

condition = input("Do you want to play 21/blackjack game? y/n ").lower()

if condition == "y":
    ga()

