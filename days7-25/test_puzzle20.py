from unittest import TestCase

from puzzle20 import Puzzle20


class TestPuzzle20(TestCase):
    pass

    def test_simple(self):
        self.assertEqual(Puzzle20.solve("5-8\n"
                                        "0-2\n"
                                        "4-7"), 3)

    def test(self):
        with open('Puzzle20.txt', 'r') as puzzle:
            Puzzle20.solve(puzzle.read())
