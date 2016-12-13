from unittest import TestCase

from puzzle1001 import Puzzle1001


class TestPuzzle1001(TestCase):
    pass

    def setUp(self):
        self.test_object = Puzzle1001()

    def test_distribute_value(self):
        self.test_object.solve("value 5 goes to bot 2")
        self.assertEqual(self.test_object.get_bot_with_values([5]), 2)

    def test_skip_instruction_when_no_values(self):
        self.test_object.solve("bot 2 gives low to bot 1 and high to bot 0")
        self.assertEqual(self.test_object.get_bot_values(2), None)

    def test_skip_instruction_when_one_value(self):
        self.test_object.solve("value 5 goes to bot 2\n"
                               "bot 2 gives low to bot 1 and high to bot 0")
        self.assertEqual(self.test_object.get_bot_values(2), [5])

    def test_bot_gives_value_when_two_available(self):
        self.test_object.solve("value 5 goes to bot 2\n"
                               "value 4 goes to bot 2\n"
                               "bot 2 gives low to bot 1 and high to bot 0")
        self.assertEqual(self.test_object.get_bot_values(0), [])
        self.assertEqual(self.test_object.get_bot_values(1), 4)
        self.assertEqual(self.test_object.get_bot_values(2), 5)
