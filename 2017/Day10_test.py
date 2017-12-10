from unittest import TestCase

from Day10 import KnotHash, part1_convert, part1_result, part2_result, part2_convert


class TestKnotHash(TestCase):
    def setUp(self):
        self.knot_hash = KnotHash()

    def test_1_1(self):
        self.assertEqual(self.knot_hash.hash(5, '3,4,1,5', part1_convert, 1, part1_result), 12)

    def test_puzzle_1(self):
        with open('Day10_puzzle.txt', 'r') as puzzle_file:
            print(self.knot_hash.hash(256, puzzle_file.read(), part1_convert, 1, part1_result))

    def test_puzzle_2(self):
        with open('Day10_puzzle.txt', 'r') as puzzle_file:
            print(self.knot_hash.hash(256, puzzle_file.read(), part2_convert, 64, part2_result))
