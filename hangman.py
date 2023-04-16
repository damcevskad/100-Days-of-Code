# Day 7
import random
import ascii_art
import word_list

chosen_word = random.choice(word_list.words)
print(ascii_art.logo)

display = []
for index in chosen_word:
    display.append("_")

lives = 6
stage = 6

guessed_letters = []

while "_" in display:
    index = 0
    guess = input("\nGuess a letter: ").lower()
    guessed_letters += guess

    if guessed_letters.count(guess) > 1:
        print("You already guessed that letter.")

    for letter in chosen_word:
        if letter == guess:
            display[index] = letter
        index += 1

    print(' '.join(display))

    if "_" not in display:
        print(f"\nYou guessed the word '{chosen_word}'! You won!")

    if guess not in chosen_word:
        stage -= 1
        lives -= 1
        print("Wrong guess.")
        print(ascii_art.stages[stage])
        if lives == 0:
            print(f"You failed to guess the word '{chosen_word}'. You lost.")
            break
    else:
        print("Good guess!")
