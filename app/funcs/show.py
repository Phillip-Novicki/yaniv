from os import system

def clear():
    _ = system('clear')

def show_hand(player, pile):
    clear()
    try:    
        print('-' * 30, '\n')
        current_top = pile.cards[-1]
        print(f'\nTop of Pile: {current_top}\n')
        print('-' * 30, '\n')
    except ValueError:
        return
    print(f"\n{player.name}'s Hand\n")
    for i in range(len(player.cards)):
        print(str(i + 1) + '.  ' + str(player.cards[i]))
    print(f'\n{player.name} currently has {player.value} points\n')
    print('-' * 30, '\n')
