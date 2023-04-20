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



