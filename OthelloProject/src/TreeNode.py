'''
Created on Feb 22, 2014

@author: dmitriostapenko
'''

class TreeNode(object):
    '''
    classdocs
    '''

    def __init__(self, boardvar, minmaxvar, numb):
    	"This initializes the node with a boardand  a string for min or max"
    	'''
    	global Board
    	global minmax
    	global children
    	'''
    	self.minmax = minmaxvar
    	self.Board = boardvar
    	self.children = []
    	self.move = [] # the actual move to get to this game state
    	self.numb = numb

    def get_numb(self):
    	return self.numb

    	#insert child into node's array
    def create_Child(self, child):
    	self.children.append(child)

    #return a child from the node
    def access_Child(self, value):
    	return self.children[value]

    #return all the children
    def return_All_Children(self):
    	return self.children

    #get min/max or -1/+1
    def get_minmax(self):
    	return self.minmax

    #return the 2d array representation of the board
    def get_Board(self):
    	return self.Board.get_2d_array()

    #return the actuall board
    def access_Board(self):
    	return self.Board

    #THIS NEEDS TO BE TESTED. NOT SURE IF OPPOSITE SHOULD BE USED
    def get_moves(self, player_color):
    	moves = self.Board.legal_moves(player_color)
    	#self.number_of_Moves = len(moves)
    	length = [0]
    	length[0] = len(moves)
    	return length

    #isnt really used anymore
    def set_moves(self):
    	moves = self.Board.legal_moves(player_color)
    	self.number_of_Moves = len(moves)

    #the 2 numbers corresponding to the move
    def get_move(self):
    	return self.move

    def set_move(self, move):
    	self.move = move



