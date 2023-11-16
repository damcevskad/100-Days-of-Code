import random
import game_data
import ascii_art


def generate_profile(profile):
    name = profile["name"]
    description = profile["description"]
    country = profile["country"]
    return f"{name}, {description} from {country}"


def check_choice(answer, a, b):
    if answer == "a":
        return a["follower_count"] > b["follower_count"]

    elif answer == "b":
        return b["follower_count"] > a["follower_count"]

    else:
        return False


def game():
    play = True
    score = 0
    second = random.choice(game_data.data)

    while play:
        first = second
        second = random.choice(game_data.data)

        while first == second:
            second = random.choice(game_data.data)

        print(f"\nA:", generate_profile(first))
        print(ascii_art.versus)
        print(f"B:", generate_profile(second))

        choice = input("\nWho has more followers? (A / B) ").lower()
        if check_choice(choice, first, second):
            score += 10
            print("Correct!")
            print(f"Score: {score}")
        else:
            print("Incorrect!")
            print(f"Final score: {score}")
            play = False


print(ascii_art.logo)
game()
