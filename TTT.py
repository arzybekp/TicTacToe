# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 00:04:05 2015

@author: russelljadams
"""
import itertools

class TTT(object):
    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])
    
    def __init__(self,squares=[]):
        if len(squares) == 0: self.squares = [None for i in range(9)]
        else: self.squares = squares
        self.player = 'X'
    
    def print_board(self):
        for element in [self.squares[i:i + 3] for i in range(0, len(self.squares), 3)]:
            print element
            
    def board_string(self):
        return list(self.squares)
            
    def available_moves(self):
        return [k for k, v in enumerate(self.squares) if v is None]
        
    def get_squares(self,player):
        return [k for k, v in enumerate(self.squares) if v == player]
        
    def make_move(self, square):
        self.squares[square] = self.player
        
    def winner(self):
        x = [i for i,k in enumerate(self.squares) if k == 'X']
        o = [i for i,k in enumerate(self.squares) if k == 'O']
        for i in itertools.combinations(x,3):
            if list(i) in self.winning_combos: return 1
        for i in itertools.combinations(o,3):
            if list(i) in self.winning_combos: return -1
        return 0
        
    def complete(self):
        if None not in self.squares: return True
        if self.winner(): return True
        return False
        
    def switch_player(self):
        if self.player == 'O': self.player = 'X'
        else: self.player = 'O'
    
            


