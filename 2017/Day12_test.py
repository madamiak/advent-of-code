from unittest import TestCase

from Day12 import DigitalPlumber


class TestDigitalPlumber(TestCase):
    def setUp(self):
        self.digital_plumber = DigitalPlumber()

    def test_1(self):
        self.assertEqual(self.digital_plumber.count_programs("0 <-> 2\n"
                                                             "1 <-> 1\n"
                                                             "2 <-> 0, 3, 4\n"
                                                             "3 <-> 2, 4\n"
                                                             "4 <-> 2, 3, 6\n"
                                                             "5 <-> 6\n"
                                                             "6 <-> 4, 5"), {0: 6, 1: 1})

    def test_puzzle(self):
        with open('Day12_puzzle.txt', 'r') as puzzle_file:
            groups = self.digital_plumber.count_programs(puzzle_file.read())
            print(groups[0])
            print(len(groups))
