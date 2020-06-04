# Student Name: Ali Al-Musawi
# Student ID: AALMUSAW
# This module creates a tic-tac-toe game.

from myBoards import *

def main():
    ###### START: Game Instructions
    print('Welcome! Tic-Tac-Toe is an amazing game to play with a friend!')
    print('The game consists of a 3x3 grid. Two players take turns. Player 1 is X. Player 2 is O.')
    print('A player wins if and only if they place 3 marks straight on a row, a column, or a diagonal.')
    print('Use a coordinate system (row, column). The top left is (1, 1) and bottom right is (3, 3) as follows:')
    for i in range(3):
        for j in range(3):
            print('| ({}, {}) '.format(i+1, j+1), end='|')
        if i != 2:
            print('\n','-'*30)
    print('\nWhen prompted to enter a coordinate, enter the row number followed by comma (or space), followed by the column number.')
    ###### END: Game Instructions

    score = ScoreBoard() # create a score board for all games.
    playAgain = True # Activate the game loop until the player does not wish to play again.
#### START: THE GAME
    while playAgain:
        game = GameBoard()  # create a new game
    #### START: Check if player's name is limited to 26 characters to keep the scoreboard looking neat.
        player1Valid = False
        player2Valid = False
        while not player1Valid:
            player1 = input('What is Player One\'s name? This is going to be X: ')
            if '\t' in player1:
                player1 = player1.replace('\t', '    ')
            if len(player1) > 26:
                print('Maximum character length is 26. Please type a shorter name.')
            else:
                player1Valid = True
        while not player2Valid:
            player2 = input('What is Player Two\'s name? This is going to be O: ')
            if '\t' in player2:
                player2 = player2.replace('\t', '    ')
            if len(player2) > 26:
                print('Maximum character length is 26. Please type a shorter name.')
            else:
                player2Valid = True
    #### END: Check if player's name is limited to 26 characters to keep the scoreboard looking neat.

        while game.decideWinner() == "?":   # While no one has won yet...
            print('It is ', player1, "'s turn.")
            ##### START: Validating X's move. Is it legal?
            XValid = False
            while not XValid:
                try:
                    Xentry = input('\nEnter the coordinate of X: ')
                    if " " in Xentry:
                        Xentry=Xentry.split()
                    elif "," in Xentry:
                        Xentry=Xentry.split(',')
                    else:
                        print('Sorry. You must follow the specified format: #,# or # # where # stands for a number 1-3.')
                        continue
                    if not (Xentry[0] in "123" and Xentry[1] in "123"):
                        print('Sorry. Your row and column numbers range from 1 to 3 inclusive.')
                        continue
                    if not game.placeX(int(Xentry[0]),int(Xentry[1])):
                        print('There is an existing mark here. Try a different coordinate.')
                        continue
                    else:
                        game.placeX(int(Xentry[0]),int(Xentry[1]))
                        XValid = True
                except (TypeError, ValueError, IndexError):
                    print('Sorry. You must follow the specified format: #,# or # # where # stands for a number 1-3.')
                    continue
            ##### END: Validating X's move. Is it legal?

            game.printCurrentBoard()

            #### START: Check if X caused the game to terminate
            if game.decideWinner() == 'X':
                break
            elif game.boardFull():
                break
            else:
                pass
            #### END: Check if X caused the game to terminate

            print('It is ', player2, "'s turn.")
            #### START: Validating O's move. Is it legal?
            OValid = False
            while not OValid:
                try:
                    Oentry = input('Enter the coordinate of O: ')
                    if " " in Oentry:
                        Oentry=Oentry.split()
                    elif "," in Oentry:
                        Oentry=Oentry.split(',')
                    else:
                        print('Sorry. You must follow the specified format: #,# or # # where # stands for a number 1-3.')
                        continue
                    if not(Oentry[0] in "123" and Oentry[1] in "123"):
                        print('Sorry. Your row and column numbers range from 1 to 3 inclusive.')
                        continue
                    if not game.placeO(int(Oentry[0]),int(Oentry[1])):
                        print('There is an existing mark here. Try a different coordinate.')
                        continue
                    else:
                        game.placeO(int(Oentry[0]),int(Oentry[1]))
                        OValid = True
                except (TypeError, ValueError, IndexError):
                    print('Sorry. You must follow the specified format: #,# or # # where # stands for a number 1-3.')
                    continue
            ##### END: Validating O's move. Is it legal?
            game.printCurrentBoard()

    ##### START: Check game status and edit the scoreboard.
        if game.decideWinner() == 'X':
            score.addWin(player1)
            score.addLoss(player2)
            print(player1, ' wins!')
        elif game.decideWinner() == 'O':
            score.addWin(player2)
            score.addLoss(player1)
            print(player2, ' wins!')
        else:
            score.addDraw(player1)
            score.addDraw(player2)
            print('A draw! That was a close one.')

        score.printScoreBoard()
    ##### END: Check game status and edit the scoreboard.

    #### START: Does the player want to play again?
        PlayAgainConfirm = input('\nWould you like to play again?  (Y/N): ')
        if not ('y' in PlayAgainConfirm or 'Y' in PlayAgainConfirm):
            playAgain=False
    #### END: Does the player want to play again?

#### END: THE GAME
    return


# Let's test the game, shall we?
main()


