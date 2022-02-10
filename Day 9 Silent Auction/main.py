
from art import logo

print("Welcome to the Silent Action!")

bids = {}
new_bidders = True

while new_bidders:
    print(logo, "\n")
    name = input("What is your name? ")
    bid = input("What is your offer? $")
    bids[name] = bid
    more_bidders = input("Are there more bidders? [y/n] ").lower()
    if more_bidders == "y":
        clear()
        continue
    else:
        new_bidders = False
winner = max(bids, key=bids.get)
print(f"The highest bidder was {winner} with ${bids[winner]}")
    