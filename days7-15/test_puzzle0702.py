from unittest import TestCase

from puzzle0702 import Puzzle0702


class TestPuzzle0702(TestCase):
    pass

    def test_support_ssl(self):
        self.assertEqual(Puzzle0702.solve("aba[bab]xyz"), 1)

    def test_not_support_ssl(self):
        self.assertEqual(Puzzle0702.solve("xyx[xyx]xyx"), 0)

    def test_with_tricky_interior_character(self):
        self.assertEqual(Puzzle0702.solve("aaa[kek]eke"), 1)

    def test_another_tricky_case(self):
        self.assertEqual(Puzzle0702.solve("zazbz[bzb]cdb"), 1)

    def test_multiline(self):
        self.assertEqual(Puzzle0702.solve("aba[bab]xyz\n"
                                          "xyx[xyx]xyx\n"
                                          "aaa[kek]eke"), 2)

    def test(self):
        with open('Puzzle07.txt', 'r') as puzzle:
            print Puzzle0702.solve(puzzle.read())
