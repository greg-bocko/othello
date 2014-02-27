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
        self.player_color = color
       
    def opponent(self):
        "Self explanatory"
        
        if self.player_color == 'B': 
            opp = OthelloPlayer('W')
        else: 
            opp = OthelloPlayer('B')
        return opp

    def heuristic_Function(self, board):
    	a = 1
    	#a needs to be illiminated from TreeNode and here
    	#print 'Alpha-Beta'
    	if(board.is_legal(self.player_color, 0, 0)):
    		return [0,0]
    	if(board.is_legal(self.player_color, 7, 0)):
    		return [7,0]
    	if(board.is_legal(self.player_color, 0, 7)):
    		return [0,7]
    	if(board.is_legal(self.player_color, 7, 7)):
    		return [7,7]
    	headNode = TreeNode(board, self.player_color, a)
    	a = self.Alpha_Beta(headNode, 0, -1000, 1000)
        print a[1], a[2]
    	#print a
    	return a[2]


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

    def Alpha_Beta(self, node, depth, alpha, beta):
    	moves = node.access_Board().legal_moves(self.player_color)
    	self.create_Children(node, moves)

    	if self.Cutoff_test(node, depth):
    		a = [0,[0,0,0,0]]
    		a[0] = node.get_moves(self.player_color)
      		return a 
    	best = [None]
    	#handles early pruning
    	counter = 0
    	children = node.return_All_Children()
    	best = [0, 0, 0 ,0, 0]
    	if(len(children) == 0):
    		return 0, best, [0,0]
    	if(self.player_color == 'B'):
    		for i in range(len(children)):
    			value = self.opponent().Alpha_Beta(children[i], depth+1, alpha, beta)
	    		if(value[0] > alpha):
	    			alpha = value[0]
	    			best = value[1]
	    			best[depth] = i
	    		elif(value[0] == alpha):
	    			a = random.randint(0,1)
	    			if(a == 1):
	    				alpha = value[0]
	    				best = value[1]
	    				best[depth] = i
	    		if (beta <= alpha):
    				break

    		if(len(children) == 0):
    			#alpha = 1000
    			return_child = [0,0]
    		else:
    			return_child = children[best[depth]].get_move()
    		#print 'yo', depth, best, len(children), alpha, beta
    		return alpha, best, return_child
    	else:
    		for i in range(len(children)):
    			value = self.opponent().Alpha_Beta(children[i], depth+1, alpha, beta)
	    		if(value[0] < beta):
	    			beta = value[0]
	    			best = value[1]
	    			best[depth] = i

	    		elif(value[0] == beta):
	    			a = random.randint(0,1)
	    			if(a == 1):
	    				beta = value[0]
	    				best = value[1]
	    				best[depth] = i
	    		
    			if (beta <= alpha):
    				break
    		if(len(children) == 0):
    			#alpha = 1000
    			return_child = [0,0]
    		else:
    			return_child = children[best[depth]].get_move()
    		#print 'hey whats up', depth, best, len(children), alpha, beta
    		return beta, best, return_child
    #creates the children of a node. Takes in moves and modifies a board for each child and creates
    #a new node for each child
    def create_Children(self, parentNode, moves):
    	parent = parentNode.access_Board()
    	for item in moves:
    		oldBoard = Board(True,parentNode.get_Board())
    		oldBoard = oldBoard.make_move(self.player_color, item[0], item[1])
    		minmaxvar = self.minmax_Opposite(parentNode.get_minmax())
    		a = random.randint(0,100)
    		newNode = TreeNode(oldBoard, minmaxvar, a)
    		newNode.set_move(item)
    		parentNode.create_Child(newNode)
    		
    def make_move(self, board):
        move = self.heuristic_Function(board)
        #print move
        board = board.make_move(self.player_color, move[0], move[1])
        print '%d %d\n' % (move[0], move[1])
        return board
        