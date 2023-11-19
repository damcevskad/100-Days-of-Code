import ascii_art
import random

print(ascii_art.logo)

print("Let's play the number guessing game!\n")
print("I'm thinking of a number between 1 - 100")
difficulty = input("Choose difficulty (easy / hard): ").lower()
secret_number = random.randint(1, 101)


def game(attempts):
    while attempts >= 0:
        number = int(input("\nGuess: "))
        if number > secret_number and attempts == 0:
            print("Too high. No more attempts.")
            print("\nBetter luck next time! You failed to guess the number. ")
            break
        elif number < secret_number and attempts == 0:
            print("Too low. No more attempts.")
            print("\nBetter luck next time! You failed to guess the number. ")
            break
        elif number > secret_number:
            print("Too high. Go lower!")
            print(f"{attempts} attempts left")
            attempts -= 1
        elif number < secret_number:
            print("Too low. Go higher!")
            print(f"{attempts} attempts left")
            attempts -= 1
        elif number == secret_number:
            print("Just right!")
            print("\nGood game. You guessed the number.")
            break
        else:
            print("Invalid input")


if difficulty == "easy":
    lives = 10
    game(lives)
elif difficulty == "hard":
    lives = 5
    game(lives)
else:
    print("Invalid input.")
    
