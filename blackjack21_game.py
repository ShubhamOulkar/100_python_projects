import random

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ga():
    cards = [random.choice(card), random.choice(card)]
    gambler = [random.choice(card), random.choice(card)]
    print(f"Your cards are {cards} and sum is {sum(cards)}.")
    print(f"Dealers 1st card is {gambler[0]}.")
    extra = input("Do you want extra card? y/n ")
    if extra == "y":
        ace0 = random.choice(card)
        cards.append(ace0)
        c = sum(cards)
        if c > 21:
            if ace0 == 11:
                cards.remove(ace0)
                ace0 = 1
                cards.append(ace0)
                c = sum(cards)
        g1 = sum(gambler)
        if g1 < 17:
            ace1 = random.choice(card)
            gambler.append(ace1)
            g = sum(gambler)
            if g > 21:
                if ace1 == 11 :
                    gambler.remove(ace1)
                    ace1 = 1
                    gambler.append(ace1)
                    g = sum(gambler)

        else:
            g = sum(gambler)

        if c > 21 and g <= 21:
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler},\n Dealer Win!")
        elif c > g and c <= 21:
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler},\n You Win!")
        elif c < g and g <= 21:
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler}, \n Dealer Win!")
        elif c == g:
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler}, \n Game Tied !")
        elif c < g and g >= 21:
            print(f"your score:{c} {cards},\ndealer score : {g} {gambler}, \n You Win!")
    else:
        c = sum(cards)
        g1 = sum(gambler)
        if g1 < 17:
            ace1 = random.choice(card)
            gambler.append(ace1)
            g = sum(gambler)
            if g > 21:
                if ace1 == 11:
                    gambler.remove(ace1)
                    ace1 = 1
                    gambler.append(ace1)
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

