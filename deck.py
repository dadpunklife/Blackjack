import random

# A class which represents a deck of 52 standard playing cards
class Deck:

    possible_values = [ 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K' ]
    possible_suits = [ 'Hearts', 'Diamonds', 'Clubs', 'Spades' ]

    cards = []
    dealt = []

    # initalize deck of 52 standard playing cards
    def __init__(self):
        for value in self.possible_values:
            for suit in self.possible_suits:
                self.cards.append(Card(value, suit))

    # shuffle the deck of cards
    def shuffle(self):
        random.shuffle(self.cards)

    # deal x number of cards from the deck and place them into the dealt pile for consistency
    def deal(self, number_of_cards):
        dealt_cards = []
        counter = range(number_of_cards)
        for instance in counter:
            card = self.cards.pop()
            dealt_cards.append(card)
        self.dealt += dealt_cards
        return dealt_cards

    # return dealt cards to deck and reshuffle it
    def reshuffle(self):
        self.cards += self.dealt
        self.dealt = []
        self.shuffle()
        

# A clas which represents a single card in a deck of standard playing cards
class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit