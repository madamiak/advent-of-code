from unittest import TestCase

from Day02 import ChecksumCalculator


class TestChecksum(TestCase):
    def setUp(self):
        self.checksum_calculator = ChecksumCalculator()

    def test_calculate_checksum(self):
        checksum = self.checksum_calculator.calculate_1("5 1 9 5\n"
                                                        "7 5 3\n"
                                                        "2 4 6 8")
        self.assertEqual(checksum, 18)

    def test_puzzle_1(self):
        with open('Day02_puzzle.txt', 'r') as puzzle_file:
            print(self.checksum_calculator.calculate_1(puzzle_file.read()))

    def test_calculate_evenly_divisible(self):
        checksum = self.checksum_calculator.calculate_2("5 9 2 8\n"
                                                        "9 4 7 3\n"
                                                        "3 8 6 5")
        self.assertEqual(checksum, 9)

    def test_puzzle_2(self):
        with open('Day02_puzzle.txt', 'r') as puzzle_file:
            print(self.checksum_calculator.calculate_2(puzzle_file.read()))
