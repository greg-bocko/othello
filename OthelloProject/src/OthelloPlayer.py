'''
Created on Feb 19, 2014

@author: gregbocko
'''

from TreeNode import TreeNode
from Board import Board
import random

class OthelloPlayer(object):
    '''
    classdocs
    '''
    

    def __init__(self, color):
        global player_color 
        player_color = color
        
       
    def opponent(self, player):
        "Self explanatory"
        
        if player == 'B': 
            opp = 'W'
        else: 
            opp = 'B'
        return opp

    def heuristic_Function(self, Board):
    	a = random.randint(0,100)
    	headNode = TreeNode(Board, 'B', a)
    	print 'got here at least'
    	a = self.Alpha_Beta(headNode, 0, [-1000], [1000], 'B')
    	print 'AB'
    	print a

    #might need to change to B/W or +1/-1
    def minmax_Opposite(self, minmaxvar):
    	if(minmaxvar == 'max'):
    		return 'min'
    	else:
    		return 'max'

    def Cutoff_test(self, state, depth):
    	if(depth >= 4):
    		return True
    	return False

    def Alpha_Beta(self, node, depth, alpha, beta, player):
    	print player
    	print node.get_numb()
    	print 'this is the board'
    	moves = node.access_Board().legal_moves(player)
    	print moves
    	self.create_Children(node, moves, player)

    	if self.Cutoff_test(node, depth):
    		#node.set_moves
    		print 'lol'
    		print node.get_moves(player)
    		return node.get_moves(player)
    	best = None
    	#handles early pruning
    	#will have to be changed

    	counter = 0
    	children = node.return_All_Children()
    	best = 0
    	if(player == 'B'):

    		for i in range(len(children)):
    			
    			children[i].access_Board().print_board()
    			#moves = child.legal_moves()
    			#child.create_Children(child, moves, player)
    			value = self.Alpha_Beta(children[i], depth+1, alpha, beta, self.opponent(player))
    			print 'this is alpha1'
    			print value
    			#if not (value == None):
	    		if(value[0] > alpha):
	    			alpha = value[0]
	    			best = i
    			if(beta[0] <= alpha[0]):
    				return [None]
    		print alpha
    		print best
    		print children[best].get_move()
    		print 'returning'
    		return alpha, best, children[best].get_move()
    	else:
    		for i in range(len(children)):

    			#node.access_Board().print_board()
    			#moves = child.legal_moves()
    			#child.create_Children(child, moves, player)
    			value = self.Alpha_Beta(children[i], depth+1, alpha, beta, self.opponent(player))
    			print 'else'
    			print value
    			#if not (value[0] == None):
	    		if(value[0] < beta):
	    			beta = value[0]
	    			best = i
    			if(beta <= alpha):
    				return [None]
    		return beta, best, children[best].get_move

    '''
    These arent being used anymore but I dont want to get rid of them yet
    def start_Build_Tree(self, Board):
    	a = random.randint(0,100)
    	headNode = TreeNode(Board, 'max', a)
    	moves = Board.legal_moves(player_color)
    	self.create_Children(headNode, moves, player_color)
    	#Board.print_board
    	children = headNode.return_All_Children()
    	#for child in children:
    		#child.access_Board().print_board()

    	self.Alpha_Beta(headNode, 0, -1000, 1000, 'W')


    
    
    def build_Tree(self, node, player_color, level):
    	if(level < 4):
    		Board = node.access_Board
    		moves = Board.legal_moves(player_color)
    		self.create_Children(node, moves, player_color)
    	else:
    		if(node.get_minmax == 'max'):
    			children = node.return_All_Children()
    			for item in children     
    		else:
    

    def create_child(self, board, parentNode, move, player):
    	newBoard = board
    	newBoard = newBoard.make_move(player, move[0], move[1])
    	minmaxvar = self.minmax_Opposite(parentNode.get_minmax())
    	a = random.randint(0,100)
    	newNode = TreeNode(newBoard, minmaxvar, a)
    	parentNode.create_Child(newNode)
    '''
    #creates the children of a node. Takes in moves and modifies a board for each child and creates
    #a new node for each child
    def create_Children(self, parentNode, moves, player):
    	parent = parentNode.access_Board()
    	for item in moves:
    		oldBoard = Board(True,parentNode.get_Board())
    		oldBoard = oldBoard.make_move(player, item[0], item[1])
    		minmaxvar = self.minmax_Opposite(parentNode.get_minmax())
    		a = random.randint(0,100)
    		newNode = TreeNode(oldBoard, minmaxvar, a)
    		newNode.set_move(item)
    		parentNode.create_Child(newNode)


    		
