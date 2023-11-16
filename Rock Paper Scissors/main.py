import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Let's play rock, paper, scissors!") 
print("'0' = rock   '1' = paper   '2' = scissors")
choice = input("Your choice: ")

computer_choice = random.randint(0, 2)

if choice == '0':
    print(rock)
    print("Computer's choice:")
    if computer_choice == 0:
        print(rock)
        print("It's a draw.")
    elif computer_choice == 1:
        print(paper)
        print("Computer wins.")
    elif computer_choice == 2:
        print(scissors)
        print("You win.")

elif choice == '1':
    print(paper)
    print("Computer's choice:")
    if computer_choice == 0:
        print(rock)
        print("You win.")
    elif computer_choice == 1:
        print(paper)
        print("It's a draw.")
    elif computer_choice == 2:
        print(scissors)
        print("Computer wins.")

elif choice == '2':
    print(scissors)
    print("Computer's choice:")
    if computer_choice == 0:
        print(rock)
        print("Computer wins.")
    elif computer_choice == 1:
        print(paper)
        print("You win.")
    elif computer_choice == 2:
        print(scissors)
        print("It's a draw.")

else:
    print("Invalid input. Computer wins.")
