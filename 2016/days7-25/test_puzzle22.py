from unittest import TestCase

from puzzle22 import Puzzle22


class TestPuzzle22(TestCase):
    pass

    def test_omit_header(self):
        self.assertEqual(0, Puzzle22.solve("root@ebhq-gridcenter# df -h\n"
                                           "Filesystem              Size  Used  Avail  Use%\n"
                                           "/dev/grid/node-x0-y0     89T   67T    22T   75%\n"))

    def test_viable_pair(self):
        self.assertEqual(1, Puzzle22.solve("root@ebhq-gridcenter# df -h\n"
                                           "Filesystem              Size  Used  Avail  Use%\n"
                                           "/dev/grid/node-x0-y0     20T   10T    10T   50%\n"
                                           "/dev/grid/node-x0-y1     20T   10T    10T   50%\n"
                                           ))

    def test_no_viable_pairs(self):
        self.assertEqual(0, Puzzle22.solve("root@ebhq-gridcenter# df -h\n"
                                           "Filesystem              Size  Used  Avail  Use%\n"
                                           "/dev/grid/node-x0-y0     30T   20T    10T   67%\n"
                                           "/dev/grid/node-x0-y1     30T   20T    10T   67%\n"
                                           ))

    def test(self):
        with open('Puzzle22.txt', 'r') as puzzle:
            print Puzzle22.solve(puzzle.read())
