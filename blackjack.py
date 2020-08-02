from deck import Deck

playDeck = Deck()

print("First card before shuffle:")
print(playDeck.cards[0].value)
print(playDeck.cards[0].suit)

playDeck.shuffle()

print("First card after shuffle:")
print(playDeck.cards[0].value)
print(playDeck.cards[0].suit)
