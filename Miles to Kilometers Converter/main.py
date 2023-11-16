from tkinter import *


def calculate():
    m = float(miles_entry.get())
    km = round(m * 1.6, 2)
    kilometers_calculated.config(text=km)


window = Tk()
window.title("Converter")
window.minsize(width=350, height=200)

miles = Label(text="Miles")
miles.grid(column=0, row=0, padx=20, pady=20)

kilometers = Label(text="Kilometers")
kilometers.grid(column=2, row=0, padx=20, pady=20)

miles_entry = Entry(width=10)
miles_entry.grid(column=0, row=1, padx=20, pady=20)

kilometers_calculated = Label()
kilometers_calculated.grid(column=2, row=1, padx=20, pady=20)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
