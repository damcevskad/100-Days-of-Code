import ascii_art
print(ascii_art.logo)
print("Welcome to the Secret Auction\n")

name = input("Enter your name: ")
bid = int(input("Enter your bid: $"))
bidders = {
    name: bid
}
other_bidders = input("Are there other bidders? ")

while other_bidders == "yes":
    name = input("\nEnter your name: ")
    bid = int(input("Enter your bid: $"))
    bidders[name] = bid
    other_bidders = input("Are there other bidders? ")

winner = ""
max_bid = 0
for key in bidders:
    if bidders[key] > max_bid:
        max_bid = bidders[key]
        winner = key

print(f"\nThe winner is {winner} with a bid of ${max_bid}!")
