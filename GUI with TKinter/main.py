from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("My 1st GUI")
window.minsize(width=500, height= 300)
window.config(padx= 100, pady= 100)

# # label
label = Label(text = "I'm a label.", font=("Arial",24,"bold"))
label.config(text= "New Text")
#label.pack(side='left')
label.place(x = 0, y = 0)
label.config(padx= 100, pady= 100)


# Button

def click():
    # label
    text = input.get()
    label.config(text= text)

button = Button(text="Click me", command = click)
button.grid(column= 3, row= 2)
button.config(padx= 2, pady= 2)

# Enter Input
input = Entry(width=10)
print(input.get())
#input.place(x= 400, y= 250)
input.grid(column=2, row=0)


# new button
new_button = Button(text="New Button", command = click)
#new_button.place(x=300,y=50)
new_button.grid(column=3, row=3)
new_button.config(padx= 5, pady= 5)
window.mainloop()
