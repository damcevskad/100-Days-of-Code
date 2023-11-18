import time
from tkinter import *
import pandas
import random

BACKGROUND = "#FFF8DE"
BROWN = "#603601"
LIGHT_BROWN = "#876445"
SAND = "#FFF8D6"
BEIGE = "#EBD8B2"

current_word = {}
to_learn = {}

def new_word():
    global current_word, timer
    window.after_cancel(timer)
    current_word = random.choice(word_dict)
    canvas.itemconfig(words, text=current_word["Deutsch"], fill=BROWN, font=("Modern", 65, "bold"))
    timer = window.after(3000, card_flip)


def card_flip():
    canvas.itemconfig(languages, text=word_data.columns[1], fill=SAND, font=("Modern", 40, "italic"))
    canvas.itemconfig(words, text=current_word["English"], fill=BEIGE, font=("Modern", 65, "bold"))
    canvas.itemconfig(card_front, image=back)


def correct_word():
    word_dict.remove(current_word)
    known = pandas.DataFrame(word_dict)
    known.to_csv("words_to_learn.csv")
    new_word()


try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original = pandas.read_csv("translated_words.csv")
    to_learn = original.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


window = Tk()
window.title("Easy German")
window.config(bg=BACKGROUND, pady=20, padx=20)
timer = window.after(3000, card_flip)

canvas = Canvas(width=700, height=500, highlightthickness=0, bg=BACKGROUND)
front = PhotoImage(file="front.png")
back = PhotoImage(file="back.png")
card_front = canvas.create_image(350, 250, image=front)

word_data = pandas.read_csv("translated_words.csv")
word_dict = word_data.to_dict(orient="records")
word = random.choice(word_data.Deutsch)

languages = canvas.create_text(350, 120, text=word_data.columns[0], fill=LIGHT_BROWN, font=("Modern", 40, "italic"))
current_word = random.choice(word_dict)
words = canvas.create_text(350, 250, text=current_word["Deutsch"], fill=BROWN, font=("Modern", 65, "bold"))
canvas.grid(row=1, column=0, columnspan=2)

correct = PhotoImage(file="correct.png")
correct_button = Button(image=correct, highlightthickness=0, command=correct_word, highlightbackground=BACKGROUND)
correct_button.grid(row=2, column=0)

incorrect = PhotoImage(file="incorrect.png")
incorrect_button = Button(image=incorrect, highlightthickness=0, command=new_word, highlightbackground=BACKGROUND)
incorrect_button.grid(row=2, column=1)

window.mainloop()
