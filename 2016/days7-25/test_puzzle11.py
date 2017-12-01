from unittest import TestCase

from puzzle11 import Puzzle11


class TestPuzzle11(TestCase):
    pass

    def test_simple(self):
        print Puzzle11.solve([['E', 'HM'], ['HG'], [], []])

    def test_parse_input(self):
        print Puzzle11.solve([['E', 'HM', 'LM'], ['HG'], ['LG'], []])

    def test(self):
        print Puzzle11.solve([['E', 'PG', 'TG', 'TM', 'QG', 'RG', 'RM', 'CG', 'CM'], ['PM', 'QM'], [], []])
