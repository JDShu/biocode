import unittest
import game
import player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = game.Game(player.Type.TEST, player.Type.AI)

    def test_damage_player(self):
        self.game.player_1.set_command("place 3")
        self.game.update()
        for x in range(11):
            self.game.do_turn()
        self.assertEqual(self.game.player_2.health, 9)
        
if __name__ == "__main__":
    unittest.main()
