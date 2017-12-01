from unittest import TestCase

from puzzle14 import Puzzle14


class TestPuzzle14(TestCase):
    pass

    def setUp(self):
        self.test_object = Puzzle14()

    def test_first_three_of_a_kind(self):
        self.test_object.solve('abc')
        self.assertEqual(18, self.test_object.get_first_candidate_index())

    def test_first_key(self):
        self.test_object.solve('abc')
        self.assertEqual(39, self.test_object.get_key_at_index(0))

    def test_64th_key(self):
        self.test_object.solve('abc')
        self.assertEqual(22728, self.test_object.get_key_at_index(63))

    def test_1(self):
        self.test_object.solve('yjdafjpo')
        print self.test_object.get_key_at_index(63)

    def test_2(self):
        self.test_object.solve('yjdafjpo', 2)
        print self.test_object.get_key_at_index(63)
