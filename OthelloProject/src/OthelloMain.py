'''
Created on Feb 19, 2014

@author: gregbocko
'''
from Board import Board

if __name__ == '__main__':
    pass

def main():
    
    board = Board()
    board.print_board()
    print board.get_touching(3,3)
    #print board.opponent('B')
    #print board.legal_moves('B')
    
main()