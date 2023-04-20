#Day 10

import ascii_art
print(ascii_art.logo)


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

while True:
    number1 = float(input("\nEnter number 1: "))
    number2 = float(input("Enter number 2: "))

    print()
    for key in operations:
        print(key)

    operation = input("\nEnter operation: ")

    calculation = operations[operation]
    result = calculation(number1, number2)

    print(f"\n{number1} {operation} {number2} = {result}")

    continuing = input("\nDo you want to keep calculating? (yes / no) ")
    if continuing == "no":
        print("Goodbye!")
        break

# ascii_art.py

logo = """
 _____________________
|  _________________  |
| |                 | |   .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| |  | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  |  | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | |  | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| |  | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | |  | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| |  | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | |  | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| |  | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | |  | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


