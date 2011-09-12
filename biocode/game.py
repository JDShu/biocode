import time

import arena
import gfx

def main():
    the_arena = arena.Arena(10,10)
    drawer = gfx.Drawer()
    turn = 0
    turn_start = time.time()
    while not the_arena.finished:
        if time.time() - turn_start > 1:
            the_arena.update()
            turn += 1
            turn_start = time.time()
            print "turn", turn
        drawer.draw(the_arena)

main()
