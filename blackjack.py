from deck import Deck

# functions...

def computeScore(hand):
    lowAceScore = 0
    highAceScore = 0
    for card in hand:
        if card.value == 'A':
            lowAceScore += 1
            highAceScore += 11
        elif card.value == 'J' or card.value == 'Q' or card.value == 'K':
            lowAceScore += 10
            highAceScore += 10
        else:
            lowAceScore += card.value
            highAceScore += card.value
    if highAceScore > 21:
        return lowAceScore
    else:
        return highAceScore

# execution...

print()
print('    *************************')
print('    * Welcome to Blackjack! *')
print('    *************************')
print()

playDeck = Deck()
playDeck.shuffle()

playerHand = []
dealerHand = []
playerScore = 0
dealerScore = 0

playerHand += playDeck.deal(2)
dealerHand += playDeck.deal(2)


print('Your hand:')
for card in playerHand:
    print('{} of {}'.format(card.value, card.suit))
print()

print('The Dealer is showing:')
print('{} of {}'.format(dealerHand[0].value, dealerHand[0].suit))
print()

playerScore = computeScore(playerHand)
print('Your current score:')
print(playerScore)
print()

print('What would you like to do?')
print('1. Hit')
print('2. Stay')
print()
choice = input()

'''
# WIP...
while playerScore < 22 or choice != 'Stay' or choice != '2':
    if choice == '1' or 'Hit':
        playerHand += playerHand.deal(1)
'''
