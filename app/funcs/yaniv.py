def yan(player1, player2):
    endgame = 0
    while player1.value <= 7:
        if player1.value < player2.value:
            print(f"\n{player1.name} Wins!!!!")
            quit()
        else:
            print(f"\n{player1.name} Loses!!!!")
            quit()
        return endgame
