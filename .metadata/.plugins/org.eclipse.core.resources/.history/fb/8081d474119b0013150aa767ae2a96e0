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
        """ BUILDS A 3X3 ARRAY THAT DESCRIBES THE BOARD AROUND the ROWth COLUMNth piece
        Arithmetic at the beginning checks that 3x3 matrix is appropriate, and if not, creates
        appropriate bounds for the bordering pieces """
        lower_i= row -1
        lower_j =column -1
        upper_i = row + 2
        upper_j = column + 2
        
        if row == 7: upper_i =8
        if column == 7: upper_j = 8
        if row == 0: lower_i = 0
        if column == 0: lower_j =0

        return [[self.GameBoard[i][j] for j in range(lower_j,upper_j)] for i in xrange(lower_j,upper_j)]

        
   # def opponent(self, player):
        
    #    return WHITE if player is BLACK else BLACK

        
        
        
    #def placeNewPiece(self):
        