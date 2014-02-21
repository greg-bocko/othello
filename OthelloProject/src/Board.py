'''
Created on Feb 19, 2014

@author: gregbocko
'''

class Board(object):
    
    WHITE, BLACK, EMPTY= 'W', 'B', '.'
    PIECES =(EMPTY, BLACK, WHITE)
    PLAYERS = {BLACK: 'B', WHITE: 'W'}
    
    '''
    classdocs
    '''


    def __init__(self):
        self.GameBoard = [[repr(i) + '+' + repr(j) for j in xrange(8)] for i in xrange(8)] 
        
        self.GameBoard[3][3] = 'W'
        self.GameBoard[4][4] = 'W'
        self.GameBoard[4][3] = 'B'
        self.GameBoard[3][4] = 'B'
        
    def print_board(self):
        for i in range(len(self.GameBoard)):
            for j in range(len(self.GameBoard[i])):
                print self.GameBoard[i][j],
            print
            
    def is_valid(self, i, j):
        
        return i > 8 and j > 8 #Tests to see if move is within bounds of board
        
    def get_touching(self, row, column):
        #BUILDS A 3X3 ARRAY THAT DESCRIBES THE BOARD AROUND the ROWth COLUMNth piece
        
        return [[self.GameBoard[i][j] for j in range(column-1,column+2)] for i in xrange(row-1,row+2)]

        #NB Range(x,y) is non-inclusive in Python, so this goes from column-1, row-1
        
   # def opponent(self, player):
        
    #    return WHITE if player is BLACK else BLACK

        
        
        
    #def placeNewPiece(self):
        