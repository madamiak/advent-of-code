from unittest import TestCase

from puzzle19 import Puzzle19


class TestPuzzle19(TestCase):
    pass

    def test_simple(self):
        self.assertEqual(Puzzle19.solve_1(5), 3)

    def test_advanced(self):
        self.assertEqual(Puzzle19.solve_1(7), 7)

    def test(self):
        print Puzzle19.solve_1(3004953)

    def test_2_simple(self):
        self.assertEqual(Puzzle19.solve_2(5), 2)

    def test_2_advanced(self):
        self.assertEqual(Puzzle19.solve_2(8), 7)

    def test_2(self):
        print Puzzle19.solve_2(3004953)
