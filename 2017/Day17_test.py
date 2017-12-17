from unittest import TestCase

from Day17 import Spinlock


class TestSpinlock(TestCase):
    def setUp(self):
        self.spinlock = Spinlock()

    def test_1(self):
        self.assertEqual(self.spinlock.next(3), 638)

    def test_puzzle(self):
        # print(self.spinlock.next(329))
        print(self.spinlock.after_first(329))
