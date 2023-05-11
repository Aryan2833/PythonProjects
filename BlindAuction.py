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
bidding_completed = False

def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_completed:
    name = input("What is your name? ")
    bidding_price = int(input("How much would you like to bid? $"))
    bids[name] = bidding_price
    should_continue = input("Are there any other bidders?Type 'Yes' or 'No'")
    if should_continue == 'No':
        bidding_completed = True
    else:
        should_continue == 'Yes'

