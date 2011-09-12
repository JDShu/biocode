import unittest
import arena
import creature

class TestArena(unittest.TestCase):

    def setUp(self):
        self.arena = arena.Arena(10,10)

    def test_add_creature(self):
        c = creature.NoobSauce()
        self.arena.add_creature(c,(0,0))
        self.assertEqual(self.arena.map[0][0], c)

    def test_creature_move(self):
        c = creature.NoobSauce()
        self.arena.add_creature(c,(0,0))
        self.arena.update()
        self.assertEqual(self.arena.map[1][0], c)
        self.assertEqual(self.arena.map[0][0], None)
        
        
if __name__=='__main__':
    unittest.main()
