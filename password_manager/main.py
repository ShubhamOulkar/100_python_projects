from tkinter import *
from tkinter import messagebox
import random
import json

# UI setup
window = Tk()
window.title("My password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)


def password_generator():
    password_generate()


def save_data():
    web = website_entry.get()
    user = Username_entry.get()
    pas = password_entry.get()

    with open('password_manager.json', 'r') as file:
        data = json.load(file)

    if web in data:
        messagebox.showinfo(title='Website Exist', message='Already present in data base')

    table = {
                web: {
                    'username': user,
                    'password': pas,
                        }
                     }

    if len(web) == 0 or len(user) == 0 or len(pas) == 0:
        messagebox.askretrycancel(title='Empty Boxes', message="Some fields are empty. \n Please check !")
    else:
        try:
            with open('password_manager.json', mode='r') as file:
                data = json.load(file)  # loading old data
        except FileNotFoundError:
            with open('password_manager.json', 'w') as file:
                json.dump(table, file, indent=4)
        else:
            data.update(table)  # updating lod data with new data
            with open('password_manager.json', 'w') as file:
                json.dump(data, file, indent=4)  # saving updated data

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            Username_entry.delete(0, END)


def website_search():
    website = website_entry.get()
    try:
        with open("password_manager.json", "r") as file:
            web_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="No data file found.")
    else:
        if website == "":
            messagebox.showinfo(title='Empty Space', message='Write website name')
        elif website in web_data:
            email = web_data[website]['username']
            password = web_data[website]['password']
            messagebox.showinfo(title=website, message=f"Username: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title='Website is not Present', message='Data is not present in file.')


website_label = Label(text='Website name:')
website_label.grid(column=0, row=1)

website_entry = Entry(width=53)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

Username_label = Label(text='Email/Username:')
Username_label.grid(column=0, row=2)

Username_entry = Entry(width=53)
Username_entry.grid(column=1, row=2, columnspan=2)
Username_entry.insert(0, "user@gmail.com")

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry = Entry(width=53)
password_entry.grid(column=1, row=3)

generatePassword_button = Button(text='Click for Password Generator', command=password_generator, width=45)
generatePassword_button.grid(column=1, row=5)

add_button = Button(text='Add to a list', width=45, command=save_data)
add_button.grid(column=1, row=6, columnspan=2)

search_button = Button(text='Search Website', width=15, command=website_search)
search_button.grid(column=3, row=1)

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

        try:
            words = random.sample(letters, num_letters)
            numb = random.sample(numbers, num_numbers)
            character = random.sample(symbols, num_char)
        except ValueError:
            messagebox.showinfo(title='Value Error', message="Input valid numbers.")
            q1_entry.delete(0, END)
            q2_entry.delete(0, END)
            q3_entry.delete(0, END)
        else:
            password = words + numb + character
            random.shuffle(password)
            show_password.delete(0, END)
            password_entry.delete(0, END)
            show_password.insert(0, "".join(password))
            password_entry.insert(0, "".join(password))

    generate_password_button = Button(text="Generate password", command=generater)
    generate_password_button.grid(column=1, row=12, columnspan=2)

    show_password = Entry(width=25)
    show_password.grid(columnspan=2, column=1, row=13)


window.mainloop()
