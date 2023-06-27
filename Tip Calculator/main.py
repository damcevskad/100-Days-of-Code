print("Welcome to the tip calculator.\n")
bill = float(input("What is the total bill? $"))
percent = int(input("How much would you like to tip? 10, 12, or 15 percent? "))
split_bill = int(input("How many people are splitting the bill? "))

percent = bill * (percent / 100)
tip = round((bill + percent) / split_bill, 2)
print(f"\nEach person should pay: ${tip}")
