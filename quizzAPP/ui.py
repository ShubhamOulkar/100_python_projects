from tkinter import *
from quiz_brain import QuizBrain
from data import selected_category, number_of_questions
THEME_COLOR = "#375362"


class Ui:

    def __init__(self, quiz: QuizBrain):
        self.quize_question = quiz
        self.window = Tk()
        self.window.title(f"{selected_category} Quizz")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score = Label(text="score:0", fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question = self.canvas.create_text(150,
                                                125,
                                                text="question",
                                                fill=THEME_COLOR,
                                                font=('Arial', 12,  'italic'),
                                                width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image= true_image, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.quize_next_question()

        self.window.mainloop()

    def quize_next_question(self):
        self.canvas.config(bg="white")
        if self.quize_question.still_has_questions():
            self.score.config(text=f"Score: {self.quize_question.score}")
            q_text = self.quize_question.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"Quizz End\n Score:{self.quize_question.score}/{number_of_questions}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        is_right = self.quize_question.check_answer('True')
        self.get_feedback(is_right)

    def false_answer(self):
        is_right = self.quize_question.check_answer('False')
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.quize_next_question)
