import pandas as pd

NATO_alphabets = pd.read_csv("nato_phonetic_alphabet.csv")

Enter_word = input("Enter a word: ").upper()

NATO_alphabet_word = {row.letter : row.code for (index, row) in NATO_alphabets.iterrows()}

ans = [NATO_alphabet_word[let] for let in Enter_word]

print(" ".join(ans))