from unittest import TestCase

from puzzle17 import Puzzle17


class TestPuzzle17(TestCase):
    pass

    def test_candidate_moves(self):
        self.assertTrue(all(x in Puzzle17.candidate_moves('hijkl') for x in ['U', 'D', 'L']))

    def test_possible_moves(self):
        self.assertEqual(['D'], Puzzle17.possible_moves('hijkl', 0, 0))

    def test_simple_1(self):
        self.assertEqual('DDRRRD', Puzzle17.solve('ihgpwlah', 0, 0))

    def test_simple_2(self):
        self.assertEqual('DDUDRLRRUDRD', Puzzle17.solve('kglvqrro', 0, 0))

    def test_simple_3(self):
        self.assertEqual('DRURDRUDDLLDLUURRDULRLDUUDDDRR', Puzzle17.solve('ulqzkmiv', 0, 0))

    def test_1(self):
        print Puzzle17.solve('hhhxzeay', 0, 0)

    def test_simple_2_1(self):
        self.assertEqual(370, Puzzle17.solve('ihgpwlah', 0, 0, 2))

    def test_simple_2_2(self):
        self.assertEqual(492, Puzzle17.solve('kglvqrro', 0, 0, 2))

    def test_simple_2_3(self):
        self.assertEqual(830, Puzzle17.solve('ulqzkmiv', 0, 0, 2))

    def test_2(self):
        print Puzzle17.solve('hhhxzeay', 0, 0, 2)
