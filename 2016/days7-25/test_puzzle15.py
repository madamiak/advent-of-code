from unittest import TestCase

from puzzle15 import Puzzle15


class TestPuzzle15(TestCase):
    pass

    def test_simple(self):
        self.assertEqual(5, Puzzle15.solve(
            'Disc #1 has 5 positions; at time=0, it is at position 4.\n'
            'Disc #2 has 2 positions; at time=0, it is at position 1.'
        ))

    def test_1(self):
        print Puzzle15.solve(
            'Disc #1 has 7 positions; at time=0, it is at position 0.\n'
            'Disc #2 has 13 positions; at time=0, it is at position 0.\n'
            'Disc #3 has 3 positions; at time=0, it is at position 2.\n'
            'Disc #4 has 5 positions; at time=0, it is at position 2.\n'
            'Disc #5 has 17 positions; at time=0, it is at position 0.\n'
            'Disc #6 has 19 positions; at time=0, it is at position 7.'
        )

    def test_2(self):
        print Puzzle15.solve(
            'Disc #1 has 7 positions; at time=0, it is at position 0.\n'
            'Disc #2 has 13 positions; at time=0, it is at position 0.\n'
            'Disc #3 has 3 positions; at time=0, it is at position 2.\n'
            'Disc #4 has 5 positions; at time=0, it is at position 2.\n'
            'Disc #5 has 17 positions; at time=0, it is at position 0.\n'
            'Disc #6 has 19 positions; at time=0, it is at position 7.\n'
            'Disc #7 has 11 positions; at time=0, it is at position 0.'
        )
