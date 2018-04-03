def rps():
    while True:

        player1 = str(input('Player 1: enter rock, paper, or scissors.: ')).lower()
        player2 = str(input('Player 2: enter rock, paper, or scissors.: ')).lower()
        correct_entries = ['rock', 'paper', 'scissors']

        if player1 in correct_entries and player2 in correct_entries:
            if player1 == player2:
                print('tie')
            elif player1 == 'rock':
                if player2 == 'scissors':
                    print('Player 1 wins')
                else:
                    print('Player 2 wins.')
            elif player1 == 'paper':
                if player2 == 'rock':
                    print('Player 1 wins.')
                else:
                    print('Player 2 wins.')
            elif player1 == 'scissors':
                if player2 == 'paper':
                    print('Player 1 wins.')
                else:
                    print('Player 2 wins.')
        else:
            print('Enter a valid input please.')


rps()
