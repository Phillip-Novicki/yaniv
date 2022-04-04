import random

suits = ('\u2661', '\u2662', '\u2660', '\u2663')
ranks = ('2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'J', 'Q', 'K', 'A', 'Joker')
#point values for each card
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
          '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
          'Q': 10, 'K': 10, 'A': 1, 'Joker': 0}
#rank values for determining if discard pile is a straight
rvalues = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
          '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11,
          'Q': 12, 'K': 13, 'A': 1, 'Joker': 0}


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.value = 0
        self.isturn = False

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value

    def lose_card(self, choice):
        card = self.cards.pop(choice)
        self.value -= values[card.rank]
        return card

        

class Card:

    def __init__(self, suit, rank, value, rvalue):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.rvalue = rvalue

    def __str__(self):
        return self.rank + ' ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                # building deck
                self.deck.append(Card(suit, rank, value=values[rank], rvalue=rvalues[rank]))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Pile():
    def __init__(self):
        self.cards = []
        for i in self.cards:
            self.card = self.cards[i]
    
    def __len__(self):
        return len(self.cards)

    def deal(self):
        single_card = self.cards.pop(-1)
        return single_card
