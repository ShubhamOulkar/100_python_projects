import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("""---------------------------------------------------------------------------------
                    Welcome to the PyPassword Generator! 2022
---------------------------------------------------------------------------------""")
nr_letters = int(input("How many letters would you like in your password? :"))
nr_symbols = int(input(f"How many symbols would you like? :"))
nr_numbers = int(input(f"How many numbers would you like? :"))

words = random.sample(letters,nr_letters)
numb = random.sample(numbers, nr_numbers)
character = random.sample(symbols, nr_symbols)

password = words + numb + character
random.shuffle(password)
print(f"Generated Password : {''.join(password)}")

print("\n-------------------- oulkarshubhu@gmail.com -------------------")
