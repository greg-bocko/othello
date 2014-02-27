import time
import copy
'''
Created on Feb 19, 2014

@author: gregbocko
'''

class Board(object):
    '''
    classdocs
    '''
    "This trick is taken from Dave Connelly"
    UP, DOWN, LEFT, RIGHT = [-1, 0],[1, 0],[0, -1],[0, 1]
    UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = [-1, -1],[1, -1], [1,1], [-1, 1]
    DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

    #if arraypresent is true, a real array should be passed in with the whole gameboard
    def __init__(self,arraypresent = False, array = []):
        if(arraypresent):
            self.GameBoard = copy.deepcopy(array)
            #this creates a copy of a gameboard array which is passed in
            
        else:
            self.GameBoard = [['.' for j in xrange(8)] for i in xrange(8)] 
            
            self.GameBoard[3][3] = 'B'
            self.GameBoard[4][4] = 'B'
            self.GameBoard[4][3] = 'W'
            self.GameBoard[3][4] = 'W'
        
    def print_board(self):
        for i in range(len(self.GameBoard)):
            for j in range(len(self.GameBoard[i])):
                print self.GameBoard[i][j],
            print
            
    def is_valid(self, row, column):
        
        return row < 8 and column < 8 and column >= 0 and row >= 0#Tests to see if move is within bounds of board
        
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

        return [[self.GameBoard[i][j] for j in range(lower_j,upper_j)] for i in xrange(lower_i,upper_i)]

        
    def opponent(self, player):
        "Self explanatory"
        
        if player == 'B': 
            opp = 'W'
        else: 
            opp = 'B'
        return opp
    
    def find_bracket(self, player, row, column, direction):

        "This method takes a square that the player wants to move to, and looks backwards to"
        "to see if there is a 'bracket' (a path of the other player's pieces bookended by"
        " one of the players own pieces) that can be formed, given a certain direction."
        
        if self.is_valid(row+direction[0], column+direction[1]):
            goingto_row = row + direction[0]
            goingto_column = column + direction[1]
        else:
            return None
        if self.GameBoard[goingto_row][goingto_column] != self.opponent(player):
            return None
        bracket = self.GameBoard[goingto_row][goingto_column]
        
        while bracket == self.opponent(player):
            goingto_row = goingto_row + direction[0]
            goingto_column = goingto_column + direction[1]
            #print 'Going to row %d column %d', (goingto_row, goingto_column)
            #if self.is_valid(goingto_row, goingto_column) and self.GameBoard[goingto_row][goingto_column] == self.opponent(player):
            if self.is_valid(goingto_row, goingto_column):
                bracket = self.GameBoard[goingto_row][goingto_column]
            else:
                #print '%d row %d column' %(goingto_row, goingto_column)
                break
        
        return None if bracket != player or not self.is_valid(goingto_row, goingto_column)  else bracket
        
        
        
        
    def make_move(self, player, row, column):
        "This method takes the row and column the player wants to make a move to, and checks in every direction"
        "from it if it can flip anything from there"
        
        if self.is_legal(player, row, column):
            self.GameBoard[row][column] = player 
            #print 'am i getting here what the frick'
        #checks that the move was legal and continues taking input if the move 
        #was not legal until legal move occurs
        else:
            print "That's _NOT_ okay, you can't treat me that way"
            sys.exit

        "Legality is checked elsewhere"
        for d in self.DIRECTIONS:
            self.make_flips(row, column, player, d)
        return self
    
    def make_flips(self, row, column, player, direction):
        "Actually does the work of flipping over the pieces along the bracket"
        
        bracket = self.find_bracket(player, row, column, direction)
        if not bracket:
            return None
        goingto_row = row + direction[0]
        goingto_column = column + direction[1]
        while self.GameBoard[goingto_row][goingto_column] != bracket:
            self.GameBoard[goingto_row][goingto_column] = player
            goingto_row = goingto_row + direction[0]
            goingto_column = goingto_column + direction[1]
        return self
    
    def is_legal(self, player, row, column):
        hasbracket = False
        
        for direction in self.DIRECTIONS:
            if self.find_bracket(player, row, column, direction) != None:
                hasbracket = True
            
        #if not hasbracket:
        #    print 'this move is illegal'

        return self.GameBoard[row][column] == '.' and hasbracket
        
            
    def legal_moves(self, player):
        "Builds table of which squares the player can legally move to, then uses that to write"
        " a list of legal moves"
        
        legal_move_table = [[self.is_legal(player, i, j) for j in range(8)] for i in range(8)] 
        legal_moves = []
        for i in range(8):
            for j in range(8):
                if legal_move_table[i][j]:
                    legal_moves.append([i, j])                  
        return legal_moves
    
    def any_legal_moves(self, player):
        #legals =self.legal_moves(player)
        if self.legal_moves(player):
            return True
        else:
            return False
    
    def read_move(self, player, row, column):
        
        if self.is_legal(player, row, column):
            self.make_move(player, row, column)
        if not self.is_legal(player, row, column):
            print "Sorry, can't do that!"
            
    def gameover(self,player):
        if self.any_legal_moves(player):
            return False
        elif self.any_legal_moves(self.opponent(player)):
            return False
        else:
            return True

    def get_2d_array(self):
        "really weird method but needs to be used when building tree"
        return self.GameBoard

    def set_2d_array(self, gb):
        "really weird method but needs to be used when building tree"
        self.GameBoard = gb

        