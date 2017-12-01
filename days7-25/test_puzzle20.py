from unittest import TestCase

from puzzle20 import Puzzle20


class TestPuzzle20(TestCase):
    pass

    def test_simple(self):
        self.assertEqual(Puzzle20.solve("5-8\n"
                                        "0-2\n"
                                        "4-7", 1), 3)

    def test_overlap(self):
        self.assertEqual(Puzzle20.solve("5-8\n"
                                        "0-7\n"
                                        "4-7", 1), 9)

    def test_neighbour(self):
        self.assertEqual(Puzzle20.solve("5-8\n"
                                        "0-4", 1), 9)

    def test(self):
        with open('Puzzle20.txt', 'r') as puzzle:
            print Puzzle20.solve(puzzle.read(), 1)

    def test_2(self):
        with open('Puzzle20.txt', 'r') as puzzle:
            print Puzzle20.solve(puzzle.read(), 2)
