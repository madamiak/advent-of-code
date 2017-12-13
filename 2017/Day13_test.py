from unittest import TestCase

from Day13 import PacketScanners


class TestPacketScanners(TestCase):
    def setUp(self):
        self.packet_scanners = PacketScanners()

    def test_1(self):
        self.assertEqual(self.packet_scanners.enter_firewall("0: 3\n"
                                                             "1: 2\n"
                                                             "4: 4\n"
                                                             "6: 4"), (0 * 3 + 6 * 4, 10))

    def test_puzzle(self):
        with open('Day13_puzzle.txt', 'r') as puzzle_file:
            print(self.packet_scanners.enter_firewall(puzzle_file.read()))
