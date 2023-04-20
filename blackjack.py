import random
import ascii_art

print(ascii_art.logo)
print("\nLet's play Blackjack! 🃏\n")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []


def first_hand():
    print(f"\nYour cards: {your_cards} Score: {your_score}")
    print(f"Computer's card: {computer_cards[0]}")


def final_hand():
    print(f"\nYour final hand: {your_cards} Score: {your_score}")
    print(f"Computer's final hand: {computer_cards} Score: {computer_score}")


def winner(score1, score2, ending_scores):
    final_hand()
    if score1 == score2:
        print("Draw!")
    elif score1 == 21:
        print("You hit the road Jack!")
    elif score2 == 21:
        print("Computer hit the road Jack!")
    elif score1 > 21:
        print("Computer wins!")
    elif score2 > 21:
        print("You win!")
    elif max(ending_scores) == score1 and not score1 > 21:
        print("You win!")
    elif max(ending_scores) == score2 and not score2 > 21:
        print("Computer wins!")


def hit_winner(score1, score2):
    final_hand()
    if score1 > 21:
        print("Computer wins!")
    elif score2 > 21:
        print("You win!")
    elif score1 == 21:
        if score1 == score2:
            print("Draw!")
        print("You hit the road Jack!")
    elif score2 == 21:
        if score1 == score2:
            print("Draw!")
        print("Computer hit the road Jack!")


def immediate_win(score1, score2):
    final_hand()
    if score1 == 21:
        print("You hit the road Jack!")
    elif score2 == 21:
        print("Computer hits the road Jack!")


while True:
    your_cards = []
    computer_cards = []

    your_card1 = random.choice(cards)
    your_card2 = random.choice(cards)
    your_cards.extend([your_card1, your_card2])
    your_score = your_card1 + your_card2

    computer_card1 = random.choice(cards)
    computer_card2 = random.choice(cards)
    computer_cards.extend([computer_card1, computer_card2])
    computer_score = computer_card1 + computer_card2

    is_winner = False

    first_hand()
    immediate_win(your_score, computer_score)
    if your_score >= 21 or computer_score >= 21:
        is_winner = True

    while not is_winner:
        is_winner = False
        hit_or_stand = input("\nHit or Stand? ").lower()

        while hit_or_stand == "hit":
            your_new_card = random.choice(cards)
            your_cards.append(your_new_card)
            your_score += your_new_card

            first_hand()
            if your_score >= 21 or computer_score >= 21:
                is_winner = True
                final_scores = [your_score, computer_score]
                winner(your_score, computer_score, final_scores)
                break
            hit_or_stand = input("\nHit or Stand? ").lower()

        else:
            final_scores = [your_score, computer_score]
            winner(your_score, computer_score, final_scores)
            is_winner = True
            break

    play_again = input("\nDo you want to play again? ")
    if play_again == "no":
        print("Thank you for playing. Goodbye!")
        break
    elif not play_again == "yes":
        print("Invalid input.")
        break
