from unittest import TestCase

from Day10 import KnotHash
from Day14 import DiskDefragmentation


class TestDiskDefragmentation(TestCase):
    def setUp(self):
        self.disk_defragmentation = DiskDefragmentation(KnotHash())

    def test_1(self):
        self.assertEqual(self.disk_defragmentation.defragment("flqrgnkx"), (8108, 1242))

    def test_puzzle(self):
        with open('Day14_puzzle.txt', 'r') as puzzle_file:
            print(self.disk_defragmentation.defragment(puzzle_file.read()))
