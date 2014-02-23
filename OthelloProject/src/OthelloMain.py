'''
Created on Feb 19, 2014

@author: gregbocko
'''
from Board import Board

if __name__ == '__main__':
    pass

def main():
    
    board = Board()
    player = 'B'
    print board.gameover(player)
    print board.legal_moves('B')
    print board.legal_moves('W')
    
    while not board.gameover(player):
        move = input()
        board.make_move(player,move[0],move[1])
        player = board.opponent(player)
        board.print_board()
        print board.legal_moves(player)
         
main()