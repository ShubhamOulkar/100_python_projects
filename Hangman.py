import random
import hangman_words
import hangman_art
print(hangman_art.logo)
words = hangman_words.word_list
A_word = random.choice(words)

dash = []
for i in range(0, len(A_word)):
    dash += '_'

lives = 6
end_game = True
while end_game is True:
    guess = input("Guess a letter: ").lower()

    for i in range(len(A_word)):
        letter = A_word[i]
        if letter == guess:
            dash[i] = letter
    if guess not in A_word:
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            end_game = False
            print("You lose")
    print(f"{' '.join(dash)}")
    if "_" not in dash:
        end_game = False
        print("You win!")
print("\n\n\n----------- oulkarshuhbu@gmail.com -------------")
