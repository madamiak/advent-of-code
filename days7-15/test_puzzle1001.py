from unittest import TestCase

from puzzle1001 import Puzzle1001


class TestPuzzle1001(TestCase):
    pass

    def setUp(self):
        self.test_object = Puzzle1001()

    def test_distribute_value(self):
        self.test_object.solve("value 5 goes to bot 2")
        self.assertEqual(self.test_object.get_bot_with_values([5]), ['bot 2'])

    def test_skip_instruction_when_no_values(self):
        self.test_object.solve("bot 2 gives low to bot 1 and high to bot 0")
        self.assertEqual(self.test_object.get_bot_values(2), None)

    def test_skip_instruction_when_one_value(self):
        self.test_object.solve("value 5 goes to bot 2\n"
                               "bot 2 gives low to bot 1 and high to bot 0")
        self.assertEqual(self.test_object.get_bot_values('bot 2'), [5])

    def test_distribute_two_values(self):
        self.test_object.solve("value 5 goes to bot 1\n"
                               "value 5 goes to bot 2\n"
                               "value 4 goes to bot 2\n")
        self.assertEqual(self.test_object.get_bot_with_values([5, 4]), ['bot 2'])
        self.assertEqual(self.test_object.get_bot_with_values([5]), ['bot 1'])

    def test_bot_gives_value_when_two_available(self):
        self.test_object.solve("value 5 goes to bot 2\n"
                               "value 4 goes to bot 2\n"
                               "bot 2 gives low to bot 1 and high to bot 0")
        self.assertEqual(self.test_object.get_bot_values('bot 1'), [4])
        self.assertEqual(self.test_object.get_bot_values('bot 0'), [5])
        self.assertEqual(self.test_object.get_bot_values('bot 2'), [])

    def test_putting_to_output(self):
        self.test_object.solve("value 5 goes to bot 2\n"
                               "value 4 goes to bot 2\n"
                               "bot 2 gives low to output 1 and high to output 0")
        self.assertEqual(self.test_object.get_bot_values('output 1'), [4])
        self.assertEqual(self.test_object.get_bot_values('output 0'), [5])
        self.assertEqual(self.test_object.get_bot_values('bot 2'), [])

    def test_complex(self):
        self.test_object.solve("value 5 goes to bot 2\n"
                               "bot 2 gives low to bot 1 and high to bot 0\n"
                               "value 3 goes to bot 1\n"
                               "bot 1 gives low to output 1 and high to bot 0\n"
                               "bot 0 gives low to output 2 and high to output 0\n"
                               "value 2 goes to bot 2")
        self.assertEqual(self.test_object.get_bot_values('output 0'), [5])
        self.assertEqual(self.test_object.get_bot_values('output 1'), [2])
        self.assertEqual(self.test_object.get_bot_values('output 2'), [3])

    def test_search_pair(self):
        bot = self.test_object.solve("value 5 goes to bot 2\n"
                                     "bot 2 gives low to bot 1 and high to bot 0\n"
                                     "value 3 goes to bot 1\n"
                                     "bot 1 gives low to output 1 and high to bot 0\n"
                                     "bot 0 gives low to output 2 and high to output 0\n"
                                     "value 2 goes to bot 2", [3, 5])
        self.assertEqual(bot, 'bot 0')

    def test_solution_1(self):
        with open('Puzzle10.txt', 'r') as puzzle:
            print self.test_object.solve(puzzle.read(), [17, 61])

    def test_solution_2(self):
        with open('Puzzle10.txt', 'r') as puzzle:
            self.test_object.solve(puzzle.read())
            out_0 = self.test_object.get_bot_values('output 0')[0]
            out_1 = self.test_object.get_bot_values('output 1')[0]
            out_2 = self.test_object.get_bot_values('output 2')[0]
            print int(out_0 * out_1 * out_2)
