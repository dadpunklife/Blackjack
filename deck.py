import random

# A class which represents a deck of 52 standard playing cards
class Deck:

    possible_values = [ 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K' ]
    possible_suits = [ 'Hearts', 'Diamonds', 'Clubs', 'Spades' ]

    cards = []

    # initalize deck of 52 standard playing cards
    def __init__(self):
        for value in self.possible_values:
            for suit in self.possible_suits:
                self.cards.append(Card(value, suit))
        print("cards created: " + str(len(self.cards)))

    # shuffle the deck of cards
    def shuffle(self):
        random.shuffle(self.cards)




# A clas which represents a single card in a deck of standard playing cards
class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
