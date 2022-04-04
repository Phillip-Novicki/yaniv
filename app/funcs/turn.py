from . import show, yaniv

def draw_card(player, deck, pile):
    while player.isturn == True:
        choice = input('Would you like to draw from the (D)eck or the (P)ile? ')
        choice = choice.lower()
        if choice[0] == 'd':
            player.add_card(deck.deal())
            player.isturn = False
        elif choice[0] == 'p':
            player.add_card(pile.deal())
            player.isturn = False
        else:
            player.isturn = True

# is_a_set determines if the cards discarded in the discard function are of a kind or a straight (3 or more cards of the 
# same suit and also in order)
def is_a_set(setlist):
    set = True
    #sort the discard pile by order of rvalue
    sortedset =sorted(setlist, key=lambda hand: int(hand.rvalue))
    while set == True:
        if len(sortedset) == 1:
            return True
        elif len(sortedset) > 1:
            for i in range(len(sortedset)):
                if i == 0:
                    continue
                if i >= 1:
                    #tests for straight with at least 3 cards of the same suit (in a row)
                    if len(sortedset)>=3 and sortedset[i].rvalue == sortedset[i - 1].rvalue + 1:
                        set = True
                        return set
                    elif sortedset[i].rank == sortedset[i-1].rank:
                        set = True
                        return set
                    
                    else:
                        set = False
                    return set


# Discard up to 5 cards. Player can discard a single card or pair or straight (3 or more cards of the same suit)
# If player does not follow suit, card will be placed back in player's hand (Determined by is_a_set)
def discard(player, opponent, deck, pile, tempset):
    setlist = tempset.cards
    current_turn = 0
    while player.isturn is True:    
        show.show_hand(player, pile)
        inp = input(f"{player.name}, Which Card(s) would you like to discard? or Type (Y)aniv or (E)xit\n"
             "press (Enter) after each selection and 'F'inish to end turn: \n")
        print('-' * 30)

        # If player choses a card
        if int(inp[0].isnumeric()):
            inp = int(inp[0]) - 1
            if (inp > -1) and (inp < len(player.cards)):
                topcard = player.lose_card(inp)
                setlist.append(topcard)
        
        # If player turn is over
        elif str(inp[0].isalpha()):
            inp = str(inp[0].lower())
            if inp[0] == 'f':
                turnover = is_a_set(setlist)
                if turnover==False:
                    add_cards_back(player, setlist)
                    setlist = []
                elif turnover==True:
                    draw_card(player, deck, pile)
                    for i in range(len(setlist)):
                        pile.cards.append(setlist[i])
                    player.isturn = False

            # If player calls "Yaniv"        
            elif inp[0] == 'y':
                yaniv.yan(player, opponent)

            # Exit game and return to terminal
            elif inp[0] == 'e':
                quit()
            else: 
                print('Player Choice invalid, please try again!')
                player.isturn = True

# Adds cards back to player's hand if discard is invalid
def add_cards_back(player, setlist):
    for i in range(len(setlist)):
        if setlist[i] not in player.cards:
            player.add_card(setlist[i])
        else:
            continue
    
def player_turn(player, opponent, deck, pile, tempset):
    player.isturn = True
    
    while player.isturn is True:
        discard(player, opponent, deck, pile, tempset)
        
    return False
