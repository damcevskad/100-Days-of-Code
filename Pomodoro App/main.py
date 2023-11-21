import math
from tkinter import *

BEIGE = "#FFF8D6"
SAND = "#83764F"
GREEN = "#A4D0A4"
DARK_GREEN = "#617A55"
LIGHT_SAND = "#A9907E"
FONT_NAME = "Times"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetition = 0
timing = None


def reset_countdown():
    global repetition
    repetition = 0
    window.after_cancel(timing)
    canvas.itemconfig(time, text="00 : 00", fill=BEIGE, font=(FONT_NAME, 35, "bold"))
    timer.config(text="timer")
    checkmark.config(text="")


def start_countdown():
    global repetition
    repetition += 1

    if repetition % 8 == 0:
        timer.config(text="long break", fg=DARK_GREEN, font=(FONT_NAME, 45, "bold"), bg=BEIGE)
        countdown(LONG_BREAK_MIN * 60)
    elif repetition % 2 == 0:
        timer.config(text="short break", fg=LIGHT_SAND, font=(FONT_NAME, 45, "bold"), bg=BEIGE)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        timer.config(text="work", fg=SAND, font=(FONT_NAME, 45, "bold"), bg=BEIGE)
        countdown(WORK_MIN * 60)


def countdown(count):
    minutes = math.floor(count / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(time, text=f"{minutes} : {seconds}")
    if count > 0:
        global timing
        timing = window.after(1000, countdown, count - 1)
    else:
        start_countdown()
        check = ""
        work = math.floor(repetition/2)
        for _ in range(work):
            check += "✓"
        checkmark.grid(row=3, column=1)
        checkmark.config(text=check)


window = Tk()
window.title("The Pomodoro App")
window.config(padx=50, pady=30, bg=BEIGE)

timer = Label(text="timer", fg=DARK_GREEN, font=(FONT_NAME, 45, "bold"), bg=BEIGE)
timer.grid(row=0, column=1)

canvas = Canvas(width=210, height=225, bg=BEIGE, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato)
time = canvas.create_text(100, 130, text="00 : 00", fill=BEIGE, font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="start", font=(FONT_NAME, 20, "bold"),
                      fg=DARK_GREEN, highlightbackground=BEIGE, command=start_countdown)
start_button.grid(row=2, column=0)

reset_button = Button(text="reset", font=(FONT_NAME, 20, "bold"),
                      fg=DARK_GREEN, highlightbackground=BEIGE, command=reset_countdown)
reset_button.grid(row=2, column=2)

checkmark = Label(text="✓", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=BEIGE)


window.mainloop()
