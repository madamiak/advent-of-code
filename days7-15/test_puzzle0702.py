from unittest import TestCase

from puzzle0702 import Puzzle0702


class TestPuzzle0702(TestCase):
    pass

    def test_support_ssl(self):
        self.assertEqual(Puzzle0702.solve("aba[bab]xyz"), 1)
