from unittest import TestCase

from puzzle12 import Puzzle12


class TestPuzzle12(TestCase):
    pass

    def setUp(self):
        self.test_object = Puzzle12()

    def test_simple(self):
        self.test_object.solve("cpy 41 a\n"
                               "jnz 1 4\n"
                               "inc a\n"
                               "inc a\n"
                               "inc a\n"
                               "inc a\n"
                               "inc a\n"
                               "inc a\n"
                               "cpy a b\n"
                               "dec a\n"
                               "jnz a -1\n"
                               "jnz a 2\n"
                               "inc a\n"
                               "jnz a 2\n"
                               "inc a")
        self.assertEqual(self.test_object.get_register('a'), 1)
        self.assertEqual(self.test_object.get_register('b'), 43)

    def test(self):
        with open('Puzzle12.txt', 'r') as puzzle:
            self.test_object.solve(puzzle.read())
            print self.test_object.get_register('a')

    def test_2(self):
        with open('Puzzle12.txt', 'r') as puzzle:
            self.test_object = Puzzle12({'a': 0, 'b': 0, 'c': 1, 'd': 0})
            self.test_object.solve(puzzle.read())
            print self.test_object.get_register('a')
