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
    print board.get_touching(7, 7)
    print board.opponent('B')
    
main()