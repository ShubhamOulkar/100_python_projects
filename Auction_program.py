import os
clear = lambda: os.system('cls')

book = {}
condition = True
while condition:
    name = input("Auctioneer name: ").lower()
    money = int(input("Auctioning money :$ "))
    book[name] = money
    ask = input("Do you have more Auctioneers? Yes/no ").lower()
    if ask == 'yes':
        condition = True
        clear()
    else:
        condition = False
        clear()

value = []
for key in book:
    value.append(book[key])

print(f"\n\nCongratulation {name}, you wins the auction by auctioning value ${max(value)}.")
