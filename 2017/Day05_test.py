from unittest import TestCase

from Day05 import MazeJumper, part_1_jump, part_2_jump


class TestMazeJumper(TestCase):
    def setUp(self):
        self.maze_jumper = MazeJumper()

    def test_1_1(self):
        self.assertEqual(self.maze_jumper.count_jumps("0\n"
                                                      "3\n"
                                                      "0\n"
                                                      "1\n"
                                                      "-3", part_1_jump), 5)

    def test_puzzle_1(self):
        with open('Day05_puzzle.txt', 'r') as puzzle_file:
            print(self.maze_jumper.count_jumps(puzzle_file.read(), part_1_jump))

    def test_2_1(self):
        self.assertEqual(self.maze_jumper.count_jumps("0\n"
                                                      "3\n"
                                                      "0\n"
                                                      "1\n"
                                                      "-3", part_2_jump), 10)

    def test_puzzle_2(self):
        with open('Day05_puzzle.txt', 'r') as puzzle_file:
            print(self.maze_jumper.count_jumps(puzzle_file.read(), part_2_jump))
