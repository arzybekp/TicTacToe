# Minimax for Tic Tac Toe

class Minimax:
    def switch_player(self, player):
        if player == 'X':
            return 'O'
        if player == 'O':
            return 'X'

    def minimax(self, game, player):
        if player == 'X':
            test = float('-inf')
            candidate = None
            for move in game.available_moves():
                game.set_square(move,player)
                val = self.min_value(game,self.switch_player(player))
                game.unset_square(move)
                if val > test:
                    test = val
                    candidate = move
            return candidate
        else:
            test = float('inf')
            candidate = None
            for move in game.available_moves():
                game.set_square(move,player)
                val = self.max_value(game,self.switch_player(player))
                game.unset_square(move)
                if val < test:
                    test = val
                    candidate = move
            return candidate


    def max_value(self, game, player):
        if game.complete():
            return game.winner()
        v = float('-inf')
        for move in game.available_moves():
            game.set_square(move, player)
            v = max([v,self.min_value(game,self.switch_player(player))])
            game.unset_square(move)
        return v

    def min_value(self, game, player):
        if game.complete():
            return game.winner()
        v = float('inf')
        for move in game.available_moves():
            game.set_square(move, player)
            v = min([v,self.max_value(game,self.switch_player(player))])
            game.unset_square(move)
        return v
