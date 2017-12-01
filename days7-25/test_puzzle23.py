from unittest import TestCase

from puzzle23 import Puzzle23


class TestPuzzle23(TestCase):
    pass

    def setUp(self):
        self.test_object = Puzzle23()

    # cpy x y
    # inc x
    # dec x
    # jnz x y
    def test_one_arg_instruction_inc(self):
        self.test_object.solve(
            "cpy 1 a\n"
            "tgl a\n"
            "inc a\n"
        )
        self.assertEqual(0, self.test_object.get_register('a'))

    def test_one_arg_instruction_dec(self):
        self.test_object.solve(
            "cpy 1 a\n"
            "tgl a\n"
            "dec a\n"
        )
        self.assertEqual(2, self.test_object.get_register('a'))

    def test_one_arg_instruction_tgl(self):
        self.test_object.solve(
            "cpy 1 a\n"
            "tgl a\n"
            "tgl a\n"
        )
        self.assertEqual(2, self.test_object.get_register('a'))

    def test_one_arg_instruction_skip_positive(self):
        self.test_object.solve(
            "cpy 2 a\n"
            "tgl a\n"
            "inc a\n"
            "tgl a\n"
        )
        self.assertEqual(4, self.test_object.get_register('a'))

    def test_two_arg_instruction_jnz(self):
        self.test_object.solve(
            "cpy 1 a\n"
            "tgl a\n"
            "jnz 3 a\n"
        )
        self.assertEqual(3, self.test_object.get_register('a'))

    def test_two_arg_instruction_cpy(self):
        self.test_object.solve(
            "cpy 7 b\n"
            "cpy 1 a\n"
            "tgl a\n"
            "cpy a b\n"
        )
        self.assertEqual(1, self.test_object.get_register('a'))
        self.assertEqual(7, self.test_object.get_register('b'))

    def test_mixed(self):
        self.test_object.solve(
            "cpy 2 a\n"
            "tgl a\n"
            "tgl a\n"
            "tgl a\n"
            "cpy 1 a\n"
            "dec a\n"
            "dec a"
        )
        self.assertEqual(3, self.test_object.get_register('a'))

    def test(self):
        with open('Puzzle23.txt', 'r') as puzzle:
            puzzle_23 = Puzzle23({'a': 7, 'b': 0, 'c': 0, 'd': 0})
            puzzle_23.solve(puzzle.read())
            print puzzle_23.get_register('a')

    def test_mul_primitive(self):
        self.test_object.solve(
            "cpy 0 a\n"
            "cpy 2 b\n"
            "cpy 0 c\n"
            "cpy 2 d\n"
            "cpy b c\n"
            "inc a\n"
            "dec c\n"
            "jnz c -2\n"
            "dec d\n"
            "jnz d -5"
        )

        self.assertEqual(4, self.test_object.get_register('a'))
        self.assertEqual(2, self.test_object.get_register('b'))
        self.assertEqual(0, self.test_object.get_register('c'))
        self.assertEqual(0, self.test_object.get_register('d'))

    def test_2(self):
        with open('Puzzle23.txt', 'r') as puzzle:
            puzzle_23 = Puzzle23({'a': 12, 'b': 0, 'c': 0, 'd': 0})
            puzzle_23.solve(puzzle.read())
            print puzzle_23.get_register('a')
