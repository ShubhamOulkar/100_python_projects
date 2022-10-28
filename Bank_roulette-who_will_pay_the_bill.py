import random
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
payer = random.randint(0,len(names))
print(f"{names[payer]} will pay the bill.")