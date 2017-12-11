from unittest import TestCase

from Day11 import HexEd


class TestHexEd(TestCase):
    def setUp(self):
        self.hex_ed = HexEd()

    def test_1(self):
        self.assertEqual(self.hex_ed.count_steps('ne,ne,ne'), (3, 3))

    def test_2(self):
        self.assertEqual(self.hex_ed.count_steps('ne,ne,sw,sw'), (0, 2))

    def test_3(self):
        self.assertEqual(self.hex_ed.count_steps('ne,ne,s,s'), (2, 2))

    def test_4(self):
        self.assertEqual(self.hex_ed.count_steps('se,sw,se,sw,sw'), (3, 3))

    def test_puzzle(self):
        with open('Day11_puzzle.txt', 'r') as puzzle_file:
            print(self.hex_ed.count_steps(puzzle_file.read()))
