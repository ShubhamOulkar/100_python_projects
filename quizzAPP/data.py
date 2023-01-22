import requests
from tkinter import *

question_data = []
category_list = ["GK", "Entertainment:books", "Entertainment:movies", "Entertainment:music",
                 "Entertainment:musicals & theater", "Entertainment:television", "Entertainment:video games",
                 "Entertainment:board games", "science and nature", "Science:Computer", "Science:Mathematics",
                 "Mythology", "Sports", "Geography", "History", "Politics", "Art", "Celebrities", "Animals", "Vehicle",
                 "Entertainment:Comics", "Science: Gadgets", "Entertainment: Japanese Anime & Manga",
                 "Entertainment: Cartoon and animations"]
category_index = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
amount_list = [5, 10, 15, 20, 30, 35, 40, 45, 50]
type_list=['boolean']
selected_category = ""
number_of_questions = ""

window = Tk()
window.title("Category Selections for quizz")

window.minsize(width=450, height= 150)

label0 = Label(text="Select Category for a quizz:")
label0.grid(row=0, column=0)
label1 = Label(text="(default category is GK.)")
label1.grid(row=0, column=2)
option0 = StringVar(window)
option0.set(category_list[0])
option0_menu = OptionMenu(window, option0, *category_list)
option0_menu.grid(row=0, column=1)


label2 = Label(text="Select number of questions:")
label2.grid(row=1, column=0)
label3 = Label(text="(default 5 question)")
label3.grid(row=1, column=2)
option1 = StringVar(window)
option1.set(str(amount_list[0]))
option1_menu = OptionMenu(window, option1, *amount_list)
option1_menu.grid(row=1, column=1)

label4 = Label(text="Select Category for a quizz:")
label4.grid(row=2, column=0)
option2 = StringVar(window)
option2.set(type_list[0])
option2_menu = OptionMenu(window, option2, *type_list)
option2_menu.grid(row=2, column=1)


def run_quizz():
    global number_of_questions
    number_of_questions = option1.get()
    global selected_category
    selected_category = option0.get()
    option0_index = category_list.index(selected_category)

    parameters = {
        "amount": number_of_questions,
        "category": category_index[option0_index],
        "type": option2.get(),
    }

    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    global question_data
    question_data = data["results"]
    window.destroy()
    return question_data, selected_category, number_of_questions


run_button = Button(text="Run Quizz", command=run_quizz)
run_button.grid(row=4, column=3)

window.mainloop()
