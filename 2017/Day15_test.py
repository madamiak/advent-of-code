from unittest import TestCase

from Day15 import DuelingGenerators


class TestDuelingGenerators(TestCase):
    def setUp(self):
        self.dueling_generators = DuelingGenerators(16807, 48271)

    def test_1(self):
        self.assertEqual(self.dueling_generators.matches("Generator A starts with 65\n"
                                                         "Generator B starts with 8921", 5), 1)

    def test_2(self):
        self.assertEqual(self.dueling_generators.matches("Generator A starts with 65\n"
                                                         "Generator B starts with 8921", 40000000), 588)

    def test_puzzle(self):
        with open('Day15_puzzle.txt', 'r') as puzzle_file:
            puzzle = puzzle_file.read()
            print(self.dueling_generators.matches(puzzle, 40000000))
            print(self.dueling_generators.matches(puzzle, 5000000, (4, 8)))
