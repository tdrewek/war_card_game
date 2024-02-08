
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.

from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("Created New Ordered Deck")
        self.all_cards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.all_cards)

    def split_in_half(self):
        return(self.all_cards[:26], self.all_cards[26:])


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        print("Creating Hand")
        self.cards = cards

    def __str__(self):
        return ("Contains {} cards".format(len(self.cards)))
    
    def add_card(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card
    
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for i in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards
    
    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards) != 0

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Create a new deck and split it in half
d = Deck()
d.shuffle()
half_one, half_two = d.split_in_half()

# Create both players
npc = Player("Computer", Hand(half_one))

name = input("What is your name? ")
user = Player(name, Hand(half_two))

total_rounds = 0
war_count = 0

while user.still_has_cards() and npc.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("Here are the current standings...")
    print(user.name + " has the count: " + str(len(user.hand.cards)))
    print(npc.name + " has the count: " + str(len(npc.hand.cards)))
    print("Play a card!\n")

    table_cards = []
    
    n_card = npc.play_card()
    u_card = user.play_card()

    table_cards.append(n_card)
    table_cards.append(u_card)

    if n_card[1] == u_card[1]:
        war_count += 1
        print("War!")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(npc.remove_war_cards())

        if RANKS.index(n_card[1]) < RANKS.index(u_card[1]):
            user.hand.add_card(table_cards)
        else:
            npc.hand.add_card(table_cards)
    else:
        if RANKS.index(n_card[1]) < RANKS.index(u_card[1]):
            user.hand.add_card(table_cards)
        else:
            npc.hand.add_card(table_cards)

# Results
print("Game Over, number of rounds: " + str(total_rounds))
print("A war happend " + str(war_count) + " times")
if user.still_has_cards():
    print("{} has won the Game with {} cards!".format(user.name, len(user.hand.cards)))
else:
    print("The Computer has won the game with {} cards!".format(len(npc.hand.cards)))