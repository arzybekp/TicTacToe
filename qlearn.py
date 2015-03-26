# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:19:41 2015

@author: russelljadams
"""
from TTT import TTT
#from minimax import Minimax
import random, os, pickle, itertools

class TTTQLearn:
    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])
        
    def __init__(self):
        self.filename = 'dictionary/qdict.p'
        if os.path.isfile(self.filename): self.qdict = pickle.load(open(self.filename, "rb"))
        else:
            self.qdict = {}
            pickle.dump(self.qdict,open(self.filename,"wb"))
        self.current_board = None
        self.alpha = .25
        self.delta = 1
            
    def save_dict(self):
        '''Save the Q-Dictionary'''
        pickle.dump(self.qdict, open(self.filename, "wb"))
        
    def str_current_board(self,board_list):
        '''Takes the board_list from TTT and makes it a string.
           This makes it easier to create a game state. More specifically
           a Q-State.'''
        string = ''
        for i in board_list: 
            if i == None: string += '_'
            else: string += str(i)
        self.current_board = string
        
    def make_hash(self, history):
        '''This takes a history, which consists of a list, the first element
           of the list is the player who moved last, the second element is
           the move they made, and the third element is a list of the current
           board configuration.'''
        self.str_current_board(history[2]) # This sets self.current_board to a string of the current board.
        return str(history[0]) + str(history[1]) + '-' + self.current_board
        
    def hash_to_board(self, _hash):
        '''This takes an already made hash, and converts it to a list
           of the current board state.'''
        board = []
        for i in _hash[3:]:
            if i == '_':board.append(None)
            else: board.append(i)
        return board
        
    def switch_player(self,player):
        return "O" if player == "X" else "X"
        
    def winner(self,board):
        x = [i for i,k in enumerate(board) if k == 'X']
        o = [i for i,k in enumerate(board) if k == 'O']
        for i in itertools.combinations(x,3):
            if list(i) in self.winning_combos: return 1
        for i in itertools.combinations(o,3):
            if list(i) in self.winning_combos: return -1
        return 0
        
    def get_successors(self, history):
        '''Returns a list of all available moves the next player can make.'''
        player = self.switch_player(history[0])
        successors = []
        copy = [i for i in self.current_board]
        for i in range(len(copy)):
            if copy[i] == '_':
                copy[i] = player
                curr = [player, i,tuple(copy)]
                successors.append(self.make_hash(curr))
                copy[i] = '_'
        return successors
        
    def update_qdict(self, board, successors):
        '''Board is the Q-state, Q(s,a). Successors are needed to find the 
           max Q(s',a') or min depending on whose turn it is. The update to Q(s,a)
           is Q(s,a) = (1-alpha) * R(Q(s,a) + (alpha * sample). Where the reward 
           function R is equivalent to self.qdict[board]. The sample is the max or min
           value of all self.qdict[successors]. Which means the update ends up being:
           (1-self.alpha) * self.qdict[board] + (self.alpha * max(self.qdict[successors]))'''
        if self.winner(self.hash_to_board(board)): return
        if board not in self.qdict:
            self.qdict[board] = self.winner(self.hash_to_board(board))
        for successor in successors:
            if successor not in self.qdict:
                self.qdict[successor] = self.winner(self.hash_to_board(successor))
        current_reward = (1 - self.alpha) * self.qdict[board]
        samples = []
        sample = None
        for successor in successors:
            #print successor, self.qdict[successor]
            samples.append(self.qdict[successor])
        if len(samples):
            if board[0] == "O": sample = max(samples)
            else: sample = min(samples)
        if sample != None:
            self.qdict[board] = current_reward + (self.alpha * sample)
            
    def best_move(self, player, board):
        '''Loops over the current board and finds all candidate moves for the
           current player. Then returns the max value or min value depending on who
           the current player is.'''
        self.str_current_board(board)
        copy = [i for i in self.current_board]
        candidates = []
        moves = []
        for i in xrange(len(copy)):
            if copy[i] == '_':
                copy[i] = player
                curr = [player, i, tuple(copy)]
                moves.append(i)
                candidates.append(self.make_hash(curr))
                copy[i] = '_'
        best = candidates[0]
        for candidate in candidates:
            if candidate in self.qdict:
                if player == 'X':
                    if self.qdict[candidate] > self.qdict[best]: best = candidate
                else:
                    if self.qdict[candidate] < self.qdict[best]: best = candidate
        return moves[candidates.index(best)]
        
def play_random(n_times):
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
            
def human_player(player):
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
    
play_random(10000)
#human_player('X')
