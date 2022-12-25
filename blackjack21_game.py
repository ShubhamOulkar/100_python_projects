import random

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ga():
    cards = [random.choice(card), random.choice(card)]
    gambler = [random.choice(card), random.choice(card)]
    print(f"Your cards {cards}")
    print(f"Dealer card {gambler}")
    extra = input("Do you want extra card? y/n ")
    if extra == "y":
        cards.append(random.choice(card))
        c = sum(cards)
        g1 = sum(gambler)
        if g1 < 17:
            gambler.append(random.choice(card))
            g = sum(gambler)
        else:
            g = sum(gambler)

        if c > 21 :
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler},\n Dealer Win!")
        elif c > g :
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler} ,\n You Win!")
        elif c < g :
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler}, \n Dealer Win!")
    else:
        c = sum(cards)
        g1 = sum(gambler)
        if g1 < 17:
            gambler.append(random.choice(card))
            g = sum(gambler)
        else:
            g = sum(gambler)

        if c > 21 and g <= 21:
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler},\n Dealer Win!")
        elif c > g and c <= 21 :
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler},\n You Win!")
        elif c < g and g <= 21:
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler}, \n Dealer Win!")
        elif c == g :
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler}, \n Game Tied !")
        elif c < g and g >= 21:
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler}, \n You Win!")




condition = input("Do you want to play 21/blackjack game? y/n ").lower()

if condition == "y":
    ga()
else:
    print("\n Thank you for visiting.")

