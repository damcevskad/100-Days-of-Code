import ascii_art
import machine_resources


def calculate_coins():
    quarters = int(input("Insert quarters: ")) * 0.25
    dimes = int(input("Insert dimes: ")) * 0.10
    nickels = int(input("Insert nickels: ")) * 0.05
    pennies = int(input("Insert pennies: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total


def check_resources(coffee):
    global machine_working
    machine_resources.resources["water"] -= machine_resources.MENU[coffee]["ingredients"]["water"]
    machine_resources.resources["coffee"] -= machine_resources.MENU[coffee]["ingredients"]["coffee"]
    machine_resources.resources["milk"] -= machine_resources.MENU[coffee]["ingredients"]["milk"]
    if machine_resources.resources["water"] <= 0 or machine_resources.resources["milk"] <= 0 or \
            machine_resources.resources["coffee"] <= 0:
        print("Not enough resources.")
        machine_working = False
    else:
        change = round(calculate_coins() - machine_resources.MENU[coffee]["cost"], 2)
        if change <= 0:
            print("\nNot enough coins provided.")
            machine_working = False
        else:
            print(f"\nYour change is: ${change}")
            print(f"Enjoy your {coffee} ☕️.")


def choose_coffee(coffee):
    global machine_working
    if coffee == "report":
        print(f"\n{'water'.title()}: {machine_resources.resources['water']}ml")
        print(f"{'milk'.title()}: {machine_resources.resources['milk']}ml")
        print(f"{'coffee'.title()}: {machine_resources.resources['coffee']}g")

    elif coffee == "espresso":
        check_resources(coffee)

    elif coffee == "cappuccino":
        check_resources(coffee)

    elif coffee == "latte":
        check_resources(coffee)

    elif coffee == "quit":
        print("\nGoodbye!")
        machine_working = False

    else:
        print("Invalid input.")
        machine_working = False


machine_working = True
print(ascii_art.logo)

while machine_working:
    choice = input("\nWhat would you like to drink? (espresso / latte / cappuccino)\n").lower()
    choose_coffee(choice)
  
