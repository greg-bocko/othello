#!/usr/bin/env python

'''
Created on Feb 26, 2014

@author: gregbocko
'''
from Board import Board
from OthelloPlayer import OthelloPlayer
from TreeNode import TreeNode
import sys

if __name__ == '__main__':
    pass

def main():
    board = Board()
    argument_line = raw_input()
    playing_dude = OthelloPlayer(argument_line[5])
    playing_dude2 = playing_dude.opponent()
    depth_limit = argument_line[7]
    time_limit1 = argument_line[9]
    time_limit2 = argument_line[11]
    this_turn = 'B'
    #if playing_dude.player_color == 'B':
    
    while not board.gameover(this_turn):
        if(board.gameover('B')):
            break
        
        if this_turn == playing_dude.player_color:
            board = playing_dude.make_move(board)
            #board.print_board()
            print '%s dude just went\n' %(this_turn)
            this_turn = trade_turn(this_turn)
            print '%s dude is going to go\n'%(this_turn)
            sys.stdout.flush()
            board.print_board()
        else:
            board = playing_dude2.make_move(board)
            board.print_board()
            print '%s dude just went\n' %(this_turn)
            this_turn = trade_turn(this_turn)
            print '%s dude is going to go\n'%(this_turn)
            sys.stdout.flush()
            board.print_board()
        '''
        else:
            #print board.legal_moves(this_turn)
            move = raw_input()
            board = board.make_move(this_turn, int(float(move[0])), int(float(move[2])))
            #print '%s dude just went\n' %(this_turn)
            this_turn = trade_turn(this_turn)
        '''
        
def trade_turn(this_turn):
    'thought about using some of the other code that does the same exact thing, but this seemed more effecient'
    'since every other way required constructing new objects etc etc'

    if this_turn == 'B': 
            opp = 'W'
    else: 
            opp = 'B'
    return opp

def understand_move(move_string):
    move = []
    move[0] = move_string[0]
    move[1] = move_string[2]
    return move
    
        
main()