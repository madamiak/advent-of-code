from unittest import TestCase

from puzzle11 import Puzzle11


class TestPuzzle11(TestCase):
    pass

    def test_parse_input(self):
        print Puzzle11.solve([['E', 'HM', 'LM'], ['HG'], ['LG'], []], 0)
