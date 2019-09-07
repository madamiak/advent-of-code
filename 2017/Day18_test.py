from unittest import TestCase

from Day18 import Duet


class TestDuet(TestCase):
    def setUp(self):
        self.duet = Duet({})

    def test_set_1(self):
        registers = {}
        self.assertEqual(self.duet.set('a', 1, registers), 1)
        self.assertEqual(registers, {'a': 1})

    def test_set_2(self):
        registers = {'a': 3}
        self.duet.set('b', 'a', registers)
        self.assertEqual(registers, {'a': 3, 'b': 3})

    def test_add_1(self):
        registers = {'a': 3}
        self.assertEqual(self.duet.add('a', 2, registers), 1)
        self.assertEqual(registers, {'a': 5})

    def test_add_2(self):
        registers = {'a': 3, 'b': 1}
        self.duet.add('a', 'b', registers)
        self.assertEqual(registers, {'a': 4, 'b': 1})

    def test_mul_1(self):
        registers = {'a': 3}
        self.assertEqual(self.duet.mul('a', 2, registers), 1)
        self.assertEqual(registers, {'a': 6})

    def test_mul_2(self):
        registers = {'a': 3}
        self.duet.mul('a', 'a', registers)
        self.assertEqual(registers, {'a': 9})

    def test_mul_3(self):
        registers = {}
        self.duet.mul('a', 'a', registers)
        self.assertEqual(registers, {'a': 0})

    def test_mod_1(self):
        registers = {'a': 3}
        self.assertEqual(self.duet.mod('a', 2, registers), 1)
        self.assertEqual(registers, {'a': 1})

    def test_mod_2(self):
        registers = {'a': 3}
        self.duet.mod('a', 'a', registers)
        self.assertEqual(registers, {'a': 0})

    def test_snd(self):
        registers = {'a': 3}
        self.assertEqual(self.duet.snd('a', registers), 1)
        self.assertEqual(self.duet.last_frequency, 3)

    def test_rcv_1(self):
        registers = {'a': 3}
        self.duet.last_frequency = 5
        self.assertEqual(self.duet.rcv('a', registers), (1, True))
        self.assertEqual(registers, {'a': 5})

    def test_rcv_2(self):
        registers = {'a': 0}
        self.duet.last_frequency = 5
        self.assertEqual(self.duet.rcv('a', registers), (1, False))
        self.assertEqual(registers, {'a': 0})

    def test_jgz_1(self):
        registers = {'a': 3}
        self.assertEqual(self.duet.jgz('a', -4, registers), -4)

    def test_jgz_2(self):
        registers = {'a': -3}
        self.assertEqual(self.duet.jgz('a', -7, registers), 1)

    def test_jgz_3(self):
        registers = {'a': 0}
        self.assertEqual(self.duet.jgz('a', -9, registers), 1)

    def test_jgz_4(self):
        registers = {'a': 3}
        self.assertEqual(self.duet.jgz('a', 'a', registers), 3)

    def test_complex(self):
        self.duet.execute("set a 1\n"
                          "add a 2\n"
                          "mul a a\n"
                          "mod a 5\n"
                          "snd a\n"
                          "set a 0\n"
                          "rcv a\n"
                          "jgz a -1\n"
                          "set a 1\n"
                          "jgz a -2")
        self.assertEqual(self.duet.last_frequency, 4)

    def test_parallel(self):
        self.duet.parallel("snd 1\n"
                           "snd 2\n"
                           "snd p\n"
                           "rcv a\n"
                           "rcv b\n"
                           "rcv c\n"
                           "rcv d\n")
        self.assertEqual(self.duet.sent_1, 3)

    def test_puzzle_pt1(self):
        with open('Day18_puzzle.txt', 'r') as puzzle_file:
            puzzle = puzzle_file.read()
            self.duet.execute(puzzle)
            print(self.duet.last_frequency)

    def test_puzzle_pt2(self):
        with open('Day18_puzzle.txt', 'r') as puzzle_file:
            puzzle = puzzle_file.read()
            self.duet.parallel(puzzle)
            print(self.duet.sent_1)
