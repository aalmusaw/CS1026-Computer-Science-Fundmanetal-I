# Student Name: Ali Al-Musawi
# Student ID: AALMUSAW
# This module implements two classes that make up the tic-tac-toe game.
# This class holds a representation of the game board throughout the running of a single game of tic-tac-toe.
class GameBoard:
    def __init__(self):
        #instance variables
        self._boardData = [[' ']*3, [' ']*3, [' ']*3] #This is where the data of the table goes.
        self._winner = '?'
        self._totalMoves = 0

    def printCurrentBoard(self):                        # Printing the current board
        print('\n\n')
        for i in range(len(self._boardData)):
            for j in range(len(self._boardData[i])):
                print('| {} '.format(self._boardData[i][j]), end='|')
            if i != 2:
                print('\n','-'*14)
        print('\n\n')
        return

    def placeX(self, i, j):     #   placing X on the board
        if self._boardData[i-1][j-1] != 'X' and self._boardData[i-1][j-1] != 'O':
            self._boardData[i-1][j-1] = 'X'
            return True
        else:
            return False

    def placeO(self, i, j):     #   placing O on the board
        if self._boardData[i-1][j-1] != 'X' and self._boardData[i-1][j-1] != 'O':
            self._boardData[i-1][j-1] = 'O'
            return True
        else:
            return False

    def decideWinner(self):
        for i in range(len(self._boardData)): #Winning by row
            if (self._boardData[i][0]+self._boardData[i][1]+self._boardData[i][2]) == 'XXX':
                self._winner = 'X'
                return self._winner
            elif (self._boardData[i][0]+self._boardData[i][1]+self._boardData[i][2]) == 'OOO':
                self._winner = 'O'
                return self._winner
            else:
                pass
        for j in range(len(self._boardData)):   #Winning by column
            if (self._boardData[0][j]+self._boardData[1][j]+self._boardData[2][j]) == 'XXX':
                self._winner = 'X'
                return self._winner
            elif (self._boardData[0][j]+self._boardData[1][j]+self._boardData[2][j]) == 'OOO':
                self._winner = 'O'
                return self._winner
            else:
                pass
        if self._boardData[0][0]+self._boardData[1][1]+self._boardData[2][2] == 'XXX' or\
            self._boardData[0][2]+self._boardData[1][1]+self._boardData[2][0] == 'XXX': # X Winning diagonally
                self._winner = 'X'
                return self._winner
        if self._boardData[0][0]+self._boardData[1][1]+self._boardData[2][2] == 'OOO' or\
            self._boardData[0][2]+self._boardData[1][1]+self._boardData[2][0] == 'OOO': # O Winning diagonally
                self._winner = 'O'
                return self._winner
        if self.boardFull():
            self._winner = '~'
        return self._winner


    def boardFull(self):                # Checking if the board is full
        self._totalMoves = 0
        for row in range(3):
            for entry in self._boardData[row]:
                if entry == "X" or entry == "O":
                    self._totalMoves = self._totalMoves + 1
        if self._totalMoves == 9:
            return True
        else:
            return False
# This class holds a representation of a score board.
class ScoreBoard:
    def __init__(self):
        self._scoreData = {'Name':[], 'Wins':{}, 'Losses':{}, 'Draws':{}} # Our Lovely Database

    def addPlayer(self, playerName):                                      # Creates players with 0 scores
        if playerName not in self._scoreData['Name']:
            self._scoreData['Name'].append(playerName)
            self._scoreData['Wins'][playerName] = 0
            self._scoreData['Losses'][playerName] = 0
            self._scoreData['Draws'][playerName] = 0

    def addWin(self, playerName):                                          # Increments a player's wins
        if playerName not in self._scoreData['Wins']:
            self.addPlayer(playerName)
        self._scoreData['Wins'][playerName] += 1

    def addLoss(self, playerName):                                          # Increments a player's losses
        if playerName not in self._scoreData['Losses']:
            self.addPlayer(playerName)
        self._scoreData['Losses'][playerName] += 1

    def addDraw(self, playerName):                                          # Increments a player's draws
        if playerName not in self._scoreData['Draws']:
            self.addPlayer(playerName)
        self._scoreData['Draws'][playerName] += 1

    def printScoreBoard(self):                                          # Prints the Scoreboard in a neat table
        print('\n\n')
        print ('-'*50)
        print('%-26s|%-7s|%-7s|%-7s|' %('Name', 'Wins', 'Losses', 'Draws'))
        print ('-'*50)
        for Name in self._scoreData['Name']:
            print('%-26s|%-7d|%-7d|%-7d|' %(Name, self._scoreData['Wins'][Name], self._scoreData['Losses'][Name], \
                                            self._scoreData['Draws'][Name]))
        print ('-'*50)
        print('\n\n')
