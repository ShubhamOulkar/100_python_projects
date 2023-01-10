from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    label.config(text= "Timer", fg = GREEN, font=(FONT_NAME, 25,'bold'))
    canvas.itemconfig(timer_text, text = "00:00")
    check_mark.config(text = " ")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps += 1

    work = WORK_MIN *60
    min_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        label.config(text="Long Break", fg=RED, background=YELLOW, font=(FONT_NAME, 35, 'bold'))

    elif reps % 2 == 0:
        count_down(min_break)
        label.config(text="Short Break", fg=PINK, background=YELLOW, font=(FONT_NAME, 35, 'bold'))

    else:
        count_down(work)
        label.config(text="Work", fg=GREEN, background=YELLOW, font=(FONT_NAME, 35, 'bold'))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minute = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text =f"{minute}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=300, height= 300)
window.config(padx= 100, pady= 100, background= YELLOW)

label = Label(text="Timer",fg=GREEN, background=YELLOW, font=(FONT_NAME,35,'bold'))
label.grid(column=1, row=0)

canvas = Canvas(width=200, height= 224, background= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",font=(FONT_NAME, 28, 'bold'))
canvas.grid(column=1,row= 1)

start_button = Button(text='Start', highlightthickness=0, command=start)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset',highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_mark = Label( fg=GREEN, background=YELLOW, font=(FONT_NAME, 12))
check_mark.grid(column=1, row= 3)


window.mainloop()