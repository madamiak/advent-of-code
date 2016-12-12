from unittest import TestCase
from puzzle08 import Puzzle08


class TestPuzzle08(TestCase):
    pass

    def setUp(self):
        self.test_object = Puzzle08()

    def test_rect(self):
        self.assertEqual(self.test_object.solve("rect 3x2"), 6)

    def test_rotate_column(self):
        self.assertEqual(self.test_object.solve("rect 3x2\n"
                                                "rotate column x=1 by 1"), 6)

    def test_rotate_row(self):
        self.assertEqual(self.test_object.solve("rect 3x2\n"
                                                "rotate row y=0 by 4"), 6)

    def test_multiple_commands(self):
        self.assertEqual(self.test_object.solve("rect 3x2\n"
                                                "rotate column x=1 by 1\n"
                                                "rotate row y=0 by 4\n"
                                                "rotate column x=1 by 1"), 6)

    def test(self):
        with open('Puzzle08.txt', 'r') as puzzle:
            print self.test_object.solve(puzzle.read(), True)
