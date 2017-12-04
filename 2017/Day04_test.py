from unittest import TestCase

from Day04 import PassphraseValidator, same_words_count, anagrams_count


class TestPassphraseValidator(TestCase):
    def setUp(self):
        self.passphrase_validator = PassphraseValidator()

    def test_1_1(self):
        self.assertEqual(self.passphrase_validator.count_valid("aa bb cc dd ee", same_words_count), 1)

    def test_1_2(self):
        self.assertEqual(self.passphrase_validator.count_valid("aa bb cc dd aa", same_words_count), 0)

    def test_1_3(self):
        self.assertEqual(self.passphrase_validator.count_valid("aa bb cc dd aaa", same_words_count), 1)

    def test_1_4(self):
        self.assertEqual(self.passphrase_validator.count_valid("aa bb cc dd ee\n"
                                                               "aa bb cc dd aa\n"
                                                               "aa bb cc dd aaa", same_words_count), 2)

    def test_puzzle_1(self):
        with open('Day04_puzzle.txt', 'r') as puzzle_file:
            print(self.passphrase_validator.count_valid(puzzle_file.read(), same_words_count))

    def test_2_1(self):
        self.assertEqual(self.passphrase_validator.count_valid("abcde fghij", anagrams_count), 1)

    def test_2_2(self):
        self.assertEqual(self.passphrase_validator.count_valid("abcde xyz ecdab", anagrams_count), 0)

    def test_2_3(self):
        self.assertEqual(self.passphrase_validator.count_valid("a ab abc abd abf abj", anagrams_count), 1)

    def test_2_4(self):
        self.assertEqual(self.passphrase_validator.count_valid("iiii oiii ooii oooi oooo", anagrams_count), 1)

    def test_2_5(self):
        self.assertEqual(self.passphrase_validator.count_valid("oiii ioii iioi iiio", anagrams_count), 0)

    def test_puzzle_2(self):
        with open('Day04_puzzle.txt', 'r') as puzzle_file:
            print(self.passphrase_validator.count_valid(puzzle_file.read(), anagrams_count))
