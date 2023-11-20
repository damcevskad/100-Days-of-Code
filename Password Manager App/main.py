from tkinter import *
from tkinter import messagebox
import random
import json

BACKGROUND = "#ededed"
GREEN = "#51884b"
BROWN = "#ca945c"
DARK_BROWN = "#83764F"


def save_login():
    login = {
        website_entry.get(): {
            "username": username_entry.get(),
            "password": password_entry.get()
        }
    }

    if len(website_entry.get()) == 0 or len(username_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo("Empty Field", message="Please don't leave empty fields.")
    else:
        try:
            with open("login.json", "r") as log:
                content = json.load(log)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("login.json", "w") as log:
                json.dump(login, log, indent=4)
        else:
            content.update(login)
            with open("login.json", "w") as log:
                json.dump(content, log, indent=4)
        finally:
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    with open("login.json", "r") as log:
        contents = json.load(log)

    if len(website_entry.get()) != 0:
        try:
            messagebox.showinfo(title=f"{website_entry.get()}",
                                message=f"Username: {contents[website_entry.get()]['username']}\n"
                                        f"Password: {contents[website_entry.get()]['password']}")
            website_entry.delete(0, END)
        except KeyError:
            messagebox.showinfo(title="Error", message="Login Info Not Found")
    else:
        messagebox.showinfo(title="Empty Field", message="Please don't leave empty fields")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    number_letters = random.randint(8, 10)
    number_symbols = random.randint(2, 4)
    number_numbers = random.randint(2, 4)

    letters_in_password = [random.choice(letters) for _ in range(number_letters)]
    symbols_in_password = [random.choice(symbols) for _ in range(number_symbols)]
    numbers_in_password = [random.choice(numbers) for _ in range(number_numbers)]

    password_list = letters_in_password + symbols_in_password + numbers_in_password
    random.shuffle(password_list)

    randomized_password = ""
    for character in password_list:
        randomized_password += character

    if password_entry.get():
        password_entry.delete(0, END)

    password_entry.insert(0, randomized_password)


window = Tk()
window.title("Password Manager")
window.config(bg=BACKGROUND, pady=30, padx=30)

canvas = Canvas(window, width=200, height=200, highlightthickness=0, bg=BACKGROUND)
logo = PhotoImage(file="MyPass_logo.png")
canvas.create_image(130, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website", bg=BACKGROUND, fg=BROWN, font=("Modern", 14, "bold"))
website.grid(column=0, row=1)
website_entry = Entry(width=21, bg=BACKGROUND, highlightbackground=BACKGROUND, fg=DARK_BROWN)
website_entry.focus()
website_entry.grid(column=1, row=1)

username = Label(text="Username", bg=BACKGROUND, fg=BROWN, font=("Modern", 14, "bold"))
username.grid(column=0, row=2)
username_entry = Entry(width=36, bg=BACKGROUND, highlightbackground=BACKGROUND, fg=DARK_BROWN)
username_entry.grid(column=1, row=2, columnspan=2)

password = Label(text="Password", bg=BACKGROUND, fg=BROWN, font=("Modern", 14, "bold"))
password.grid(column=0, row=3)
password_entry = Entry(width=21, bg=BACKGROUND, highlightbackground=BACKGROUND, fg=DARK_BROWN)
password_entry.grid(column=1, row=3)

generator_button = Button(text="Generate Password", fg=GREEN, highlightbackground=BACKGROUND,
                          font=("Modern", 12, "normal"), command=generate_password, width=12)
generator_button.grid(column=2, row=3)

search_button = Button(text="Search", fg=GREEN, highlightbackground=BACKGROUND,
                       font=("Modern", 12, "normal"), command=search, width=12)
search_button.grid(column=2, row=1)

add_button = Button(text="Add Password", fg=GREEN, highlightbackground=BACKGROUND, font=("Modern", 12, "normal"),
                    command=save_login, width=37)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
