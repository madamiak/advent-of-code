from unittest import TestCase
from puzzle0901 import Puzzle0901


class TestPuzzle0901(TestCase):
    pass

    def test_no_compression(self):
        self.assertEqual(Puzzle0901.solve("ADVENT"), 6)

    def test_simple_decompression_one_block(self):
        self.assertEqual(Puzzle0901.solve("A(1x5)BC"), 7)

    def test_simple_decompression_two_blocks(self):
        self.assertEqual(Puzzle0901.solve("(3x3)XYZ"), 9)

    def test_decompression_two_markers(self):
        self.assertEqual(Puzzle0901.solve("A(2x2)BCD(2x2)EFG"), 11)

    def test_misleading_marker(self):
        self.assertEqual(Puzzle0901.solve("(6x1)(1x3)A"), 6)

    def test_tricky_marker_multiplier(self):
        self.assertEqual(Puzzle0901.solve("X(8x2)(3x3)ABCY"), 18)

    def test(self):
        with open('Puzzle09.txt', 'r') as puzzle:
            print Puzzle0901.solve(puzzle)
