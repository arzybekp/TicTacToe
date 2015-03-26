# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:06:02 2015

@author: russelljadams
"""

from TTT import TTT
from qlearn import TTTQLearn
from minimax import Minimax
import random

def Q_play_random(n_times):
    '''This just trains the Q-Dictionary by playing randomly. This probably isn't optimal.
       Implementing an e-greedy algorithm would be better.'''
    Q = TTTQLearn()
    for i in range(n_times):
        t = TTT()
        while not t.complete():
            current = [t.player]
            move = random.choice(t.available_moves())
            current.append(move)
            t.make_move(move)
            current.append(tuple(t.board_string()))
            t.switch_player()
            
            board = Q.make_hash(current)
            successors = Q.get_successors(current)
            Q.update_qdict(board,successors)
    Q.save_dict()
          
def Q_human_player(player):
    Q = TTTQLearn()
    t = TTT()
    t.print_board()
    while not t.complete():
        current = [t.player]
        if player == t.player:
            move = input("please enter a move: ")
        else:
            move = Q.best_move(t.player, t.board_string())
        current.append(move)
        t.make_move(move)
        t.print_board()
        print
        current.append(tuple(t.board_string()))
        t.switch_player()
        
        board = Q.make_hash(current)
        successors = Q.get_successors(current)
        Q.update_qdict(board, successors)
    Q.save_dict()
    
def minimax_human(player):
    t = TTT()
    m = Minimax()
    t.print_board()
    while not t.complete():
        if player == t.player:
            move = input("Please enter a move: ")
        else:
            move = m.minimax(t, t.player)
        t.make_move(move)
        t.switch_player()
        t.print_board()
        print
Q_human_player('O')
minimax_human('O')