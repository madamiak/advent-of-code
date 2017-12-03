from unittest import TestCase

from Day03 import Spiral


class TestSpiral(TestCase):
    def setUp(self):
        self.spiral = Spiral()

    def test_1_1(self):
        self.assertEqual(self.spiral.distance(1), 0)

    def test_1_2(self):
        self.assertEqual(self.spiral.distance(12), 3)

    def test_1_3(self):
        self.assertEqual(self.spiral.distance(23), 2)

    def test_1_4(self):
        self.assertEqual(self.spiral.distance(1024), 31)

    def test_puzzle_1(self):
        with open('Day03_puzzle.txt', 'r') as puzzle_file:
            print(self.spiral.distance(puzzle_file.read()))

    def test_2_1(self):
        self.assertEqual(self.spiral.value(2), 4)

    def test_2_2(self):
        self.assertEqual(self.spiral.value(5), 10)

    def test_puzzle_2(self):
        with open('Day03_puzzle.txt', 'r') as puzzle_file:
            print(self.spiral.value(puzzle_file.read()))

