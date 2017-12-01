from unittest import TestCase

from puzzle13 import Puzzle13


class TestPuzzle13(TestCase):
    pass

    def test_simple(self):
        print Puzzle13.solve(9, 6, 7, 4, 10)

    def test(self):
        print Puzzle13.solve(45, 45, 31, 39, 1364, part=2)
