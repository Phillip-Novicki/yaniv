import models 
from funcs import turn


while True:
    #counter keeps track of player turn
    counter = 0

    print('\nThis is Yaniv!!!')
    n = input('Enter Your Name: ')
    print('\n')
    c = 'Computer'
    
    
    # Create & Shuffle the deck, deal five cards to each player
    deck = models.Deck()
    pile = models.Pile()
    deck.shuffle()


    # Initialize players and deal each player 5 cards off the top of the deck
    player_one = models.Player(n)
    for i in range(5):
        player_one.add_card(deck.deal())

    player_two = models.Player(c)
    for i in range(5):
        player_two.add_card(deck.deal())

    #Burn one
    pile.cards.append(deck.deal())

    #Gameplay
    while counter < 2:

        tempset = models.Pile()

        if counter == 0:
            turn.player_turn(player_one, player_two, deck, pile, tempset)
            counter = counter + 1
        elif counter == 1:
            turn.player_turn(player_two, player_one, deck, pile, tempset)
            counter = counter - 1

    





