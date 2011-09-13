import time

import arena
import gfx
import player
import base

PLAYER_DICT = {player.Type.HUMAN: player.Human,
               player.Type.AI: player.AI,
               player.Type.TEST: player.Test}

class Game:

    def __init__(self, player_1, player_2):
        self.game_arena = arena.Arena(10,10)
        self.drawer = gfx.Drawer()
        self.turn = 0
        self.turn_start = time.time()
        self.player_1 = PLAYER_DICT[player_1](1)
        self.player_1.base = base.LEFT
        self.player_2 = PLAYER_DICT[player_2](2)
        self.player_2.base = base.RIGHT
        
    def main(self):
        while not self.game_arena.finished:
            self.update()

    def update(self):
        self.player_1.scan_input()
        self.player_1.act(self.game_arena)
        self.player_2.act(self.game_arena)
        if time.time() - self.turn_start > 1:
            self.do_turn()
        self.drawer.draw(self.game_arena)

    def do_turn(self):
        self.game_arena.update()
        self.game_arena.execute_results(self.player_1, self.player_2)
        self.turn += 1
        self.turn_start = time.time()
        print "turn", self.turn
       
if __name__ == "__main__":
    g = Game(player.Type.HUMAN, player.Type.AI)
    g.main()