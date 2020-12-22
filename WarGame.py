import random

# Global Variables 
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5, 'Six' : 6, 'Seven' : 7, 'Eight' : 8, 
'Nine' : 9, 'Ten' : 10, 'Jack' : 11, 'Queen' : 12, 'King' : 13, 'Ace' : 14}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # create card object
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]): 
            # List of multiple card objects
            self.all_cards.extend(new_cards)

        else:
            # Single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# GAME SETUP
player_one = Player('One')
player_two = Player('Two')

# Create deck and Shuffle
new_deck = Deck()
new_deck.shuffle()

# Split the deck in two
for card in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# Game On
game_on = True
round = 0

while game_on:
    
    round += 1
    print(f'Round number {round}')

    # Check first if either player has zero cards
    if (len(player_one.all_cards) == 0):
        print('Player one out of cards. Player two WINS!')
        game_on = False
        break
    if (len(player_two.all_cards) == 0):
        print('Player two out of cards. Player one WINS!')
        game_on = False
        break

    # Create empty lists for player one and two, add card for each player by removing 1 from deck
    player_one_hand = []
    player_one_hand.append(player_one.remove_one())

    player_two_hand = []
    player_two_hand.append(player_two.remove_one())

    at_war = True

    while at_war:

        print(f'Player One dealt {player_one_hand[-1]}')
        print(f'Player Two dealt {player_two_hand[-1]}')

        # Check for greater value in player1 and 2 hand
        # if player 1 has greater value, player gets all cards added to end of pile 
        if player_one_hand[-1].value > player_two_hand[-1].value:
            player_one.add_cards(player_one_hand)
            player_one.add_cards(player_two_hand)
            print('Player One wins this round.')
            print(player_one)
            print('\n')
            at_war = False

        # Check for greater value in player1 and 2 hand
        # if player 2 has greater value, player gets all cards added to end of pile
        elif player_one_hand[-1].value < player_two_hand[-1].value:
            player_two.add_cards(player_one_hand)
            player_two.add_cards(player_two_hand)
            print('Player Two wins this round.')
            print(player_two)
            print('\n')
            at_war = False

        else:
            # Case when both card values are the same, then war is declared
            # another card is grabbed and compared
            print("WAR! WAR! WAR!")

            # Check must be made first to see if either player has enough cards
            if len(player_one.all_cards) < 5:
                print('Player One does not have enough cards. Player Two WINS!')
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('Player Two does not have enough cards. Player One WINS!')
                game_on = False
                break

            else:
                # Add the next five cards to each players hand and compare them
                for card in range(5):
                    player_one_hand.append(player_one.remove_one())
                    player_two_hand.append(player_two.remove_one())
