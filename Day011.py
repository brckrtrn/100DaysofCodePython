import random
from replit import clear

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal(card_number):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = []
    for i in range(card_number):
        chosen_card.append(random.choice(cards))
    return chosen_card

def score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def result(your_cards, computer_cards):
    your_score = score(your_cards)
    computer_score = score(computer_cards)

    if your_score > 21:
        print("You lost!")
    elif computer_score > 21:
        print("You win!")
    elif your_score > computer_score:
        print("You win!")
    elif your_score == computer_score:
        print("Draw!")
    else:
        print("You lost!")

def blackjack():
    your_cards = deal(2)
    computer_cards = deal(2)
    print(logo)

    is_game_over = False

    while not is_game_over:
        your_score = score(your_cards)
        computer_score = score(computer_cards)
   
        print(f"Your cards: {your_cards}, current score: {your_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if your_score == 0 or computer_score == 0 or your_score > 21:
            is_game_over = True
        else:
            new_card = input("Type 'y'to get another card, type 'n' to pass: ")
            if new_card == "y":
                your_cards += deal(1)
            else:
                is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards += deal(1)
            computer_score = score(computer_cards)

        print(f"Your final hand: {your_cards}, final score: {your_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            
        result(your_cards, computer_cards)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    blackjack()
