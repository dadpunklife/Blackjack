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

def isBusting(hand):
    if computeScore(hand) > 21:
        return True
    else:
        return False

def dealerTurn(playerHand, dealerHand):
    while computeScore(dealerHand) < computeScore(playerHand):
        dealerHand += playDeck.deal(1)
        if isBusting(dealerHand):
            return False
    return True

# execution...

print()
print('    *************************')
print('    * Welcome to Blackjack! *')
print('    *************************')
print()

playDeck = Deck()
playDeck.shuffle()
isGame = True
choice = ''
isChoiceStay = False
isBusted = False

while isGame:
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

    while computeScore(playerHand) < 22 and not isChoiceStay:
        print('What would you like to do?')
        print('1. Hit')
        print('2. Stay')
        print()
        choice = input()

        if choice == '1' or choice.lower() == 'hit':
            playerHand += playDeck.deal(1)
            print('Your hand:')
            for card in playerHand:
                print('{} of {}'.format(card.value, card.suit))
            print()

            playerScore = computeScore(playerHand)
            print('Your current score:')
            print(playerScore)
            print()

            if isBusting(playerHand):
                print('Stop busting so much')
                isBusted = True
                #Do you want to play again?

        elif choice == '2' or choice.lower() == 'stay':
            isChoiceStay = True

            # Here is where the dealer decides to hit or stay
            dealerWon = dealerTurn(playerHand, dealerHand)
            if dealerWon:
                print('Your hand:')
                for card in playerHand:
                    print('{} of {}'.format(card.value, card.suit))
                print()
                playerScore = computeScore(playerHand)
                print('Your current score:')
                print(playerScore)
                print()

                print('Dealer\'s hand:')
                for card in dealerHand:
                    print('{} of {}'.format(card.value, card.suit))
                print()
                dealerScore = computeScore(dealerHand)
                print('Dealer\'s current score:')
                print(dealerScore)
                print()

                print('The dealer won!')
            
            else:
                print('Your hand:')
                for card in playerHand:
                    print('{} of {}'.format(card.value, card.suit))
                print()
                playerScore = computeScore(playerHand)
                print('Your current score:')
                print(playerScore)
                print()

                print('Dealer\'s hand:')
                for card in dealerHand:
                    print('{} of {}'.format(card.value, card.suit))
                print()
                dealerScore = computeScore(dealerHand)
                print('Dealer\'s current score:')
                print(dealerScore)
                print()

                print('You won!')

        else:
            print('Enter a proper answer')
    
    playDeck.reshuffle()
    isChoiceStay = False
    isBusted = False

    print('Do you want to play again?')
    choice = input()
    if choice.lower() == 'no':
        isGame = False