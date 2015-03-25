# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:19:41 2015

@author: russelljadams
"""
from TTT import TTT
from minimax import Minimax

t = TTT()
m = Minimax()

#while not t.complete():
#    move = m.minimax(t,'X')
#    t.make_move(move,'X')
#    t.print_board()
#    print
#    move = raw_input('please choose a move: ')
#    t.make_move(int(move),'O')
#    
#t = TTT()
#while not t.complete():
#    t.print_board()
#    print
#    move = raw_input('please choose a move: ')
#    t.make_move(int(move),'X')
#    move = m.minimax(t,'O')
#    t.make_move(move,'O')
#    t.print_board()
#    print

first= 'O'
history = []
while not t.complete():
    first = t.switch_player(first)
    current = [first]
    current.append(t.board_string())
    
    t.print_board()
    print
    
    move = m.minimax(t,first)
    current.append(move)
    t.make_move(move,first)
    
    history.append(current)

for i in history:
    print sorted(i)
    print