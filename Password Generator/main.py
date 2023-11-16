import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
number_letters = int(input("Enter number of letters: "))
number_symbols = int(input("Enter number of symbols: "))
number_numbers = int(input("Enter number of numbers: "))

password_length = number_letters + number_symbols + number_numbers

letters_in_password = ""
for letter in range(0, number_letters):
    letters_in_password += random.choice(letters)

symbols_in_password = ""
for symbol in range(0, number_symbols):
    symbols_in_password += random.choice(symbols)

numbers_in_password = ""
for number in range(0, number_numbers):
    numbers_in_password += random.choice(numbers)

not_randomized_password = letters_in_password + symbols_in_password + numbers_in_password

password_list = list(not_randomized_password)
random.shuffle(password_list)

randomized_password = ""
for character in password_list:
    randomized_password += character

print(f"\nYour new generated password is: {randomized_password}")
