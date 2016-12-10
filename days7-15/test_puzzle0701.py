from unittest import TestCase
from puzzle0701 import Puzzle0701


class TestPuzzle0701(TestCase):
    pass

    def test_support_tls(self):
        self.assertEqual(Puzzle0701.solve("abba[mnop]qrst"), 1)

    def test_not_support_tls(self):
        self.assertEqual(Puzzle0701.solve("abcd[bddb]xyyx"), 0)

    def test_not_support_tls_when_identical_interior_chars(self):
        self.assertEqual(Puzzle0701.solve("aaaa[qwer]tyui"), 0)

    def test_support_tls_when_inside_bigger_not_reversed_string(self):
        self.assertEqual(Puzzle0701.solve("ioxxoj[asdfgh]zxcvbn"), 1)

    def test_multiple_strings(self):
        self.assertEqual(Puzzle0701.solve("abba[mnop]qrst\n"
                                          "abcd[bddb]xyyx\n"
                                          "oxxo[asdfgh]zxcvbn"), 2)

    def test(self):
        with open('Puzzle07.txt', 'r') as puzzle:
            print Puzzle0701.solve(puzzle.read())
