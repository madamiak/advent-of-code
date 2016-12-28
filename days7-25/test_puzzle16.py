from unittest import TestCase

from puzzle16 import Puzzle16


class TestPuzzle16(TestCase):
    pass

    def setUp(self):
        self.test_object = Puzzle16()

    def test_1_100(self):
        self.assertEqual('100', self.test_object.generate_random_data('1'))

    def test_0_001(self):
        self.assertEqual('001', self.test_object.generate_random_data('0'))

    def test_11111_11111000000(self):
        self.assertEqual('11111000000', self.test_object.generate_random_data('11111'))

    def test_111100001010_1111000010100101011110000(self):
        self.assertEqual('1111000010100101011110000', self.test_object.generate_random_data('111100001010'))

    def test_checksum_110010110100_100(self):
        self.assertEqual('100', self.test_object.generate_checksum('110010110100'))

    def test_disk_20_10000(self):
        self.assertEqual('01100', self.test_object.solve(20, '10000'))

    def test_1(self):
        print self.test_object.solve(272, '11101000110010100')

    def test_2(self):
        print self.test_object.solve(35651584, '11101000110010100')
