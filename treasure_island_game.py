print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

path = input("Choose your path: left or right? (left / right)\n")
if path.lower() == "left":
    print("You have chosen left.")
    print("You are the sea. You need to arrive at the shore.")
    sea = input("Choose your path: Wait for the boat to arrive or swim to shore. (boat / swim)\n")
    if sea == "boat":
        print("You have chosen to wait for the boat.")
        print("You just arrived to shore.")
        chests = input("In front of you are three treasure chests. Red, blue and yellow. Choose carefully. (red / "
                       "green / yellow)\nle"
                       "le")
        if chests == "red":
            print("You have chosen the red chest.")
            print("You were blown up by the TNT. Game over.")
            print("*********************************************")
        elif chests == "green":
            print("You have chosen the green chest.")
            print("You were attacked by snakes. Game over.")
            print("*********************************************")
        else:
            print("You have chosen the yellow chest.")
            print("*********************************************")
            print("Congratulations! You have found the treasure!")
            print("*********************************************")
    else:
        print("You have chosen to swim to shore.")
        print("You were eaten by a shark. Game over.")
        print("*********************************************")

elif path.lower() == "right":
    print("You have chosen right.")
    print("You just fell into a hole. Game over.")
    print("*********************************************")

else:
    print("Invalid input. Game over.")
    print("*********************************************")
