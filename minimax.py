class Minimax:
    def __init__(self):
        pass
    def minimax(self, game, player):
        if player == 'X':
            test = float('-inf')
            candidate = None
            for move in game.available_moves():
                game.make_move(move,player)
                val = self.min_value(game,game.switch_player(player))
                game.make_move(move,None)
                if val > test:
                    test = val
                    candidate = move
            return candidate
        else:
            test = float('inf')
            candidate = None
            for move in game.available_moves():
                game.make_move(move,player)
                val = self.max_value(game,game.switch_player(player))
                game.make_move(move,None)
                if val < test:
                    test = val
                    candidate = move
            return candidate
            
    
    def max_value(self, game, player):
        if game.complete():
            return game.winner()
        v = float('-inf')
        for move in game.available_moves():
            game.make_move(move,player)
            v = max([v,self.min_value(game,game.switch_player(player))])
            game.make_move(move,None)
        return v
    
    def min_value(self, game, player):    
        if game.complete():
            return game.winner()
        v = float('inf')
        for move in game.available_moves():
            game.make_move(move,player)
            v = min([v,self.max_value(game,game.switch_player(player))])
            game.make_move(move,None)
        return v
