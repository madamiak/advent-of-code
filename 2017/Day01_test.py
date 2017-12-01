from unittest import TestCase

from Day01 import Captcha


class Test(TestCase):
    def setUp(self):
        self.captcha = Captcha()

    def test_calculate_captcha_1(self):
        self.assertEqual(self.captcha.solve('1122'), 3)

    def test_calculate_captcha_2(self):
        self.assertEqual(self.captcha.solve('1111'), 4)

    def test_calculate_captcha_3(self):
        self.assertEqual(self.captcha.solve('1234'), 0)

    def test_calculate_captcha_4(self):
        self.assertEqual(self.captcha.solve('91212129'), 9)

    def test_puzzle_1(self):
        puzzle_file = open('Day01_puzzle.txt', 'r')
        print(self.captcha.solve(puzzle_file.readline()))
        puzzle_file.close()

    def test_puzzle_2(self):
        puzzle_file = open('Day01_puzzle.txt', 'r')
        digits = puzzle_file.readline()
        print(self.captcha.solve(digits, int(len(digits) / 2)))
        puzzle_file.close()
