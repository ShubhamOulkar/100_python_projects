from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("Mile to Kilometers converter")
window.minsize(width=300, height= 300)
window.config(padx= 100, pady= 100)
kilometer = 0
def calculation():
    value = entry.get()
    kilometer = float(value) * 1.609
    label3 = Label(text=round(kilometer,2), font=("Arial", 10, "bold"))
    label3.grid(column=1, row=1)

entry = Entry(width= 10)
entry.grid(column=1, row=0)

label0 = Label(text = "Miles", font=("Arial",10,"bold"))
label0.grid(column=2, row=0)

label1 = Label(text = "is equal to", font=("Arial",10,"bold"))
label1.grid(column=0, row=1)

label2 = Label(text = "km", font=("Arial",10,"bold"))
label2.grid(column=2, row=1)

label4 = Label(text="0", font=("Arial", 10, "bold"))
label4.grid(column=1, row=1)

button = Button(text="Calculate", command = calculation)
button.grid(column=1, row=2)






window.mainloop()