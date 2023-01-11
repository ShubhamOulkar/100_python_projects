from tkinter import *
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generate():
    q1 = Label(text="How many letters would you like in your password?\n(a to z)", font=('Arial', 10))
    q1.grid(column=1, row=8)

    q1_entry = Entry(width=5)
    q1_entry.grid(column=2, row=8)

    q2 = Label(text=f"\nHow many numbers would you like in your password?\n{numbers}", font=('Arial', 10))
    q2.grid(column=1, row=9)

    q2_entry = Entry(width=5)
    q2_entry.grid(column=2, row=9)

    q3 = Label(text=f"\nHow many symbols wold you like in your password? \n{symbols}", font=('Arial', 10))
    q3.grid(column=1, row=10)

    q3_entry = Entry(width=5)
    q3_entry.grid(column=2, row=10)


    def generater():
        num_letters = int(q1_entry.get())
        num_numbers = int(q2_entry.get())
        num_char = int(q3_entry.get())

        words = random.sample(letters, num_letters)
        numb = random.sample(numbers, num_numbers)
        character = random.sample(symbols, num_char)

        password = words + numb + character
        random.shuffle(password)
        show_password.delete(0, END)
        show_password.insert(0, password)


    generate_password_button = Button(text="Generate password", command= generater)
    generate_password_button.grid(column=1, row=12, columnspan=2)

    show_password = Entry(width=25)
    show_password.grid(columnspan=2, column=1, row=13)
