#
# w = int(input("Weight: "))
# h = float(input("Height: "))
#
#
# if  w > 200 or h > 3 or w == 0 or h == 0:
#     raise ValueError("Input valid height or weight.")
#
# bmi = w / h **2
# print(bmi)




import pandas as pd

NATO_alphabets = pd.read_csv("C:\\Users\\Admin\\PycharmProjects\\100_python_projects\\Day 25\\nato_phonetic_alphabet.csv")


NATO_alphabet_word = {row.letter: row.code for (index, row) in NATO_alphabets.iterrows()}

def generate():
    Enter_word = input("Enter a word: ").upper()
    try :
        ans = [NATO_alphabet_word[let] for let in Enter_word]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        generate()
    else:
        print(" ".join(ans))

generate()