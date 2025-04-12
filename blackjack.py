import random
import sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

def Main():
    print("Welcome to Blackjack!")
    print("How much money do you want to start with?")
    money = input("$")
    while True:
        if money <= 0:
            print("You are broke!")
            print("Thank God you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()
        print("Money: ", money)

def GetPlayerBet(maxBet):
    while True:
        print("How much do you want to bet? (1-{}, or QUIT)".format(maxBet))
        bet = input("$").upper().strip()
        if bet == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def GetGameDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K','A'):
            deck.append(rank,suit)
    random.shuffle(deck)
    return deck

def DisplayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print("DEALER:", GetHandleValue(dealerHand))

def GetHandleValue(cards):
    value = 0
    numOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            numOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)
    
    value += numOfAces
    for i in range(numOfAces):
        if value + 10 <= 21:
            value += 10
    return value

def DisplayCards(cards):
    rows = ['','','','','']

    for i, card in enumerate(cards):
        for i, card in enumerate(cards):
            rows[0] += '___'

if __name__ == "__main__":
    Main()