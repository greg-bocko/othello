'''
Created on Feb 19, 2014

@author: gregbocko
'''
from Board import Board
from OthelloPlayer import OthelloPlayer
from TreeNode import TreeNode

if __name__ == '__main__':
    pass

def main():
    
    board = Board()
    player = 'B'
    print board.gameover(player)
    print board.legal_moves('B')
    print board.legal_moves('W')
    
    #print board.print_board

    player1 = OthelloPlayer('B')
    player1.heuristic_Function(board)
    #node = TreeNode(board, 1)
    #player1.Alpha_Beta(node, 0, -1000, 1000, +1)
    
    print 'hi'

    while not board.gameover(player):
        move = input()
        #board.make_move(player,move[0],move[1])
        player = board.opponent(player)
        board.print_board()
        print board.legal_moves(player)

main()