# Import needed modules
import random

# Define starting logo
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

# Define a deck of cards and shuffle them
full_deck = ([i for i in range(1,11)]*4)
full_deck.extend(['J', 'Q', 'K', 'A']*4)
random.shuffle(full_deck)

# Function to deal starting hands
def deal_hand(deck, num_cards):
    '''Function takes in the remaining deck as an input, assuming the deck is shuffled.
    The first two elements are popped from the deck and returned as a hand.
    The remaining deck after hand removal is also returned.'''
    hand = [deck.pop(0) for elem in range(num_cards)]
    return hand, deck

# Function to calculate scoring
def calc_score(hand):
    '''Function takes in a hand of any length. The number of aces are counted upfront
    as these are treated differently depending on the total score of the remaining cards.
    If a card is not an ace, we simply tally up its value into the score. If there are aces,
    each ace contributes 11 points unless this will lead to a total greater than 21, in 
    which case, the ace is made to count only one point.'''
    # Initialize the ace counter and score
    ace_count = hand.count("A")
    score = 0

    # For each card in the hand, tally up the score - ignore aces for now
    for card in hand:
        if card not in ("J", "Q", "K", "A"):
            score += card
        elif card in ("J", "Q", "K"):
            score += 10

    # For each ace, adjust the score according to the total observed thus far
    for _ in range(ace_count):
        if score + 11 > 21:
            score += 1
        else:
            score += 11
    
    # Check if blackjack or bust
    blackjack = False
    bust = False
    if score == 21:
        blackjack = True
    elif score > 21:
        bust = True

    # Output the final hand's score
    return score, blackjack, bust

# Function to handle outputting of results 
def show_results(hand, score, player):
    print(f"{player}'s hand: {hand}. {player}'s score: {score}.")


# Deal hands - start with the full deck and deal for the dealer and the user
print(logo)
curr_deck = full_deck.copy()
dealer_hand, curr_deck = deal_hand(curr_deck, 2)
user_hand, curr_deck = deal_hand(curr_deck, 2)

# User to continue drawing cards while they still want to
done = False
while not done:
    print(f"Your hand is {user_hand}")
    print(f"The dealer's first card is {dealer_hand[0]}")

    # Calculate dealer and user scores, and whether there's a winner yet
    dealer_score, dealer_blackjack, dealer_bust = calc_score(dealer_hand)
    user_score, user_blackjack, user_bust = calc_score(user_hand)

    # Determine if anyone has won or lost thus far
    if dealer_blackjack:
        print("Dealer blackjack! Dealer wins!")
        done = True
    elif user_blackjack:
        print("Player blackjack! Player wins!")
        done = True
    elif user_bust:
        print("Player exceeds 21! Dealer wins!")
        done = True
    # If nobody has won or lost yet, prompt for if the user wants another card
    else:
        another_card = input("Would you like to draw another card? Y/N? ").lower()
        # If no user cards wanted further, draw cards for the dealer - assume input is correct
        if another_card == 'n':
            done = True
            # If dealer < 17 then draw more cards
            while dealer_score < 17:
                new_card, curr_deck = deal_hand(curr_deck, 1)
                dealer_hand = dealer_hand + new_card
                dealer_score, dealer_blackjack, dealer_bust = calc_score(dealer_hand)
            
        # If further cards wanted, draw another card and add to user hand
        else:
            new_card, curr_deck = deal_hand(curr_deck, 1)
            user_hand = user_hand + new_card
    print("______________________________________")

# Tally up game
show_results(dealer_hand, dealer_score, "Dealer")
show_results(user_hand, user_score, "User")
            
# Final results
if dealer_bust:
    print("Dealer exceeds 21! Player wins!")
elif dealer_score > user_score:
    print("Dealer score higher than player's! Dealer wins!")
elif dealer_score < user_score:
    print("Player score higher than dealer's! Player wins!")
else:
    print("Player score equals dealer score! Draw!")