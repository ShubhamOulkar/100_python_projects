from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("My 1st GUI")
window.minsize(width=500, height= 300)

# # label
label = Label(text = "I'm a label.", font=("Arial",24,"bold"))
label.pack()
label['text'] = 'New Text'
label.config(text= "New Text")

# Button

def click():
    # label
    text = input.get()
    label.config(text= text)

button = Button(text="Click me", command = click)
button.pack()

# Enter Input
input = Entry(width=10)
input.pack()
print(input.get())










window.mainloop()
