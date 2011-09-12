import time

import arena
import gfx
import player

def main():
    game_arena = arena.Arena(10,10)
    drawer = gfx.Drawer()
    turn = 0
    turn_start = time.time()
    game_player = player.Human(0)
    ai_player = player.AI(1)
    while not game_arena.finished:
        game_player.scan_input()
        game_player.act(game_arena)
        if time.time() - turn_start > 1:
            game_arena.update()
            turn += 1
            turn_start = time.time()
            print "turn", turn
        drawer.draw(game_arena)

main()
