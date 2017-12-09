from unittest import TestCase

from Day09 import StreamEvaluator


class TestStreamEvaluator(TestCase):
    def setUp(self):
        self.stream_evaluator = StreamEvaluator()

    def test_1(self):
        self.assertEqual(self.stream_evaluator.eval('{}'), (1, 0))

    def test_2(self):
        self.assertEqual(self.stream_evaluator.eval('{{{}}}'), (1 + 2 + 3, 0))

    def test_3(self):
        self.assertEqual(self.stream_evaluator.eval('{{},{}}'), (1 + 2 + 2, 0))

    def test_4(self):
        self.assertEqual(self.stream_evaluator.eval('{{{},{},{{}}}}'), (1 + 2 + 3 + 3 + 3 + 4, 0))

    def test_5(self):
        self.assertEqual(self.stream_evaluator.eval('{<a>,<a>,<a>,<a>}'), (1, 4))

    def test_6(self):
        self.assertEqual(self.stream_evaluator.eval('{{<ab>},{<ab>},{<ab>},{<ab>}}'), (1 + 2 + 2 + 2 + 2, 8))

    def test_7(self):
        self.assertEqual(self.stream_evaluator.eval('{{<!!>},{<!!>},{<!!>},{<!!>}}'), (1 + 2 + 2 + 2 + 2, 0))

    def test_8(self):
        self.assertEqual(self.stream_evaluator.eval('{{<a!>},{<a!>},{<a!>},{<ab>}}'), (1 + 2, 17))

    def test_9(self):
        self.assertEqual(self.stream_evaluator.eval('{{<!>},{<!>},{<!>},{<a>}}'), (1 + 2, 13))

    def test_10(self):
        self.assertEqual(self.stream_evaluator.eval('<random characters>'), (0, 17))

    def test_11(self):
        self.assertEqual(self.stream_evaluator.eval('<<<<>'), (0, 3))

    def test_12(self):
        self.assertEqual(self.stream_evaluator.eval('<{!>}>'), (0, 2))

    def test_13(self):
        self.assertEqual(self.stream_evaluator.eval('<!!>'), (0, 0))

    def test_14(self):
        self.assertEqual(self.stream_evaluator.eval('<!!!>>'), (0, 0))

    def test_15(self):
        self.assertEqual(self.stream_evaluator.eval('<{o"i!a,<{i<a>'), (0, 10))

    def test_puzzle(self):
        with open('Day09_puzzle.txt', 'r') as puzzle_file:
            print(self.stream_evaluator.eval(puzzle_file.read()))
