from unittest import TestCase

from Day06 import BankBalancer


class TestBankBalancer(TestCase):
    def setUp(self):
        self.bank_balancer = BankBalancer()

    def test_1(self):
        self.assertEqual(self.bank_balancer.count_cycles('0\t2\t7\t0'), (5, 4))

    def test_puzzle(self):
        with open('Day06_puzzle.txt', 'r') as puzzle_file:
            print(self.bank_balancer.count_cycles(puzzle_file.read()))
