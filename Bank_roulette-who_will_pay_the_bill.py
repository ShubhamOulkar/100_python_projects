import random
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
# payer = random.randint(0,len(names) - 1)
# print(f"{names[payer]} will pay the bill.")

payer = random.choice(names)
print(f"{payer} will pay the bill.")