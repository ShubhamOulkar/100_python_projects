from tkinter import *
from tkinter import  messagebox
import password_generater

# UI setup
window = Tk()
window.title("My password Manager")
window.config(padx= 50, pady= 50)

canvas = Canvas(width=200, height= 200)
img = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = img)
canvas.grid(column=1, row=0)


def password_generator():
    password_generater.password_generate()


def save_data():
    web = website_entry.get()
    user = Username_entry.get()
    pas = password_entry.get()

    if len(web) == 0 or len(user) == 0 or len(pas) == 0:
        messagebox.askretrycancel(title= 'Empty Boxes', message= "Some fields are empty. \n Please check !")
    else:
        table = f'| {web} |' + f' {user} ' + f'| {pas} |\n'
        messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {user} \nPassword: {pas}")

        with open('password_manager.txt', mode= 'a') as  file:
            file.write(table)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            Username_entry.delete(0, END)



website_label = Label(text='Website name:')
website_label.grid(column=0, row=1)

website_entry = Entry(width= 53)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

Username_label = Label(text='Email/Username:')
Username_label.grid(column=0, row=2)

Username_entry = Entry(width= 53)
Username_entry.grid(column=1, row=2, columnspan= 2)
Username_entry.insert(0,"user@gmail.com")

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry = Entry(width=53)
password_entry.grid(column=1, row= 3)

generatePassword_button = Button(text='Click for Password Generator', command=password_generator, width=45)
generatePassword_button.grid(column= 1, row= 5)

add_button = Button(text='Add to a list', width= 45, command=save_data)
add_button.grid(column=1, row=6, columnspan=2)



window.mainloop()