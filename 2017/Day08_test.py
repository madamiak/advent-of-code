from unittest import TestCase

from Day08 import InstructionExecutor


class TestInstructionExecutor(TestCase):
    def setUp(self):
        self.instruction_executor = InstructionExecutor()

    def test_1(self):
        self.assertEqual(self.instruction_executor.execute("b inc 5 if a > 1\n"
                                                           "a inc 1 if b < 5\n"
                                                           "c dec -10 if a >= 1\n"
                                                           "c inc -20 if c == 10"), (1, 10))

    def test_puzzle(self):
        with open('Day08_puzzle.txt', 'r') as puzzle_file:
            print(self.instruction_executor.execute(puzzle_file.read()))
