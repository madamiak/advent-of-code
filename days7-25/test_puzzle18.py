from unittest import TestCase

from puzzle18 import Puzzle18


class TestPuzzle18(TestCase):
    pass

    def setUp(self):
        self.test_object = Puzzle18()

    def test_next_row(self):
        self.test_object.solve('..^^.', 2)
        self.assertEqual('.^^^^', self.test_object.get_row(1))

    def test_next_rows(self):
        self.test_object.solve('.^^.^.^^^^', 10)
        self.assertEqual('^^.^^^..^^', self.test_object.get_row(9))

    def test_sum_safe_tiles(self):
        self.assertEqual(38, self.test_object.solve('.^^.^.^^^^', 10))

    def test_1(self):
        print self.test_object.solve('^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......', 40)

    def test_2(self):
        print self.test_object.solve('^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......', 400000)
