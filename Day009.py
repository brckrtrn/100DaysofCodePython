from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}
is_new_bidder_exists = True

while is_new_bidder_exists:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid

    new_bidder = input("Are there any other biiders? Type 'yes' or 'no'.\n").lower()
    if new_bidder == "yes":
        clear()
    elif new_bidder == "no":
        is_new_bidder_exists = False

max_bid = 0

for key in bids:
    if bids[key] > max_bid:
        max_bid = bids[key]
        winner_name = key
        winner_bid =  bids[key]

print(f"The winner is {winner_name} with a bid of ${winner_bid}")