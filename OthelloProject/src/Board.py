'''
Created on Feb 19, 2014

@author: gregbocko
'''

class Board(object):
    '''
    classdocs
    '''


    def __init__(self):
        Board = [['.' for i in xrange(8)] for j in xrange(8)] 
        
        Board[4][4] = 'W'
        Board[5][5] = 'W'
        Board[5][4] = 'B'
        Board[4][5] = 'B'
        
    def printBoard(self):
        for i in (0, 7):
            for j in (0, 7):
                print Board[i][j]
            print '\ln'
            
    def getBoardState(self):
        return Board