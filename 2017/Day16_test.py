from unittest import TestCase

from Day16 import PermutationPromenade


class TestPermutationPromenade(TestCase):
    def setUp(self):
        self.permuatation_promenade = PermutationPromenade()

    def test_spin(self):
        self.assertEqual(self.permuatation_promenade.dance("s3", 5), "cdeab")

    def test_exchange(self):
        self.assertEqual(self.permuatation_promenade.dance("x0/1", 5), "bacde")

    def test_partner(self):
        self.assertEqual(self.permuatation_promenade.dance("pa/b", 5), "bacde")

    def test_dance(self):
        self.assertEqual(self.permuatation_promenade.dance("s1,x3/4,pe/b", 5), "baedc")

    def test_puzzle(self):
        with open('Day16_puzzle.txt', 'r') as puzzle_file:
            puzzle = puzzle_file.read()
            # print(self.permuatation_promenade.dance(puzzle, 16))
            print(self.permuatation_promenade.dance(puzzle, 16, 1000000000))


