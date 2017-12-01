from unittest import TestCase

from puzzle09 import Puzzle09


class TestPuzzle09(TestCase):
    pass

    def test_no_compression(self):
        self.assertEqual(Puzzle09.solve("ADVENT"), 6)

    def test_simple_decompression_one_block(self):
        self.assertEqual(Puzzle09.solve("A(1x5)BC"), 7)

    def test_simple_decompression_two_blocks(self):
        self.assertEqual(Puzzle09.solve("(3x3)XYZ"), 9)

    def test_decompression_two_markers(self):
        self.assertEqual(Puzzle09.solve("A(2x2)BCD(2x2)EFG"), 11)

    def test_misleading_marker(self):
        self.assertEqual(Puzzle09.solve("(6x1)(1x3)A"), 6)

    def test_tricky_marker_multiplier(self):
        self.assertEqual(Puzzle09.solve("X(8x2)(3x3)ABCY"), 18)

    def test(self):
        with open('Puzzle09.txt', 'r') as puzzle:
            print Puzzle09.solve(puzzle.read())

    def test_simple_decompression_one_block_2(self):
        self.assertEqual(Puzzle09.solve("(3x3)XYZ", solution_1=False), 9)

    def test_simple_nested_marker(self):
        self.assertEqual(Puzzle09.solve("X(8x2)(3x3)ABCY", solution_1=False), 20)

    def test_multiple_nested_markers(self):
        self.assertEqual(Puzzle09.solve("(27x12)(20x12)(13x14)(7x10)(1x12)A", solution_1=False), 241920)

    def test_mixed_multiple_nested_markers(self):
        self.assertEqual(Puzzle09.solve("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", solution_1=False),
                         445)

    def test_2(self):
        with open('Puzzle09.txt', 'r') as puzzle:
            print Puzzle09.solve(puzzle.read(), solution_1=False)
