from unittest import TestCase

from Day19 import SeriesOfTubes

diagram = "     |          \n" \
          "     |  +--+    \n" \
          "     A  |  C    \n" \
          " F---|----E|--+ \n" \
          "     |  |  |  D \n" \
          "     +B-+  +--+ "


class TestSeriesOfTubes(TestCase):
    def setUp(self):
        self.series_of_tubes = SeriesOfTubes()

    def test_go_down_by_only_line_connected_to_the_top(self):
        self.series_of_tubes.follow_routing_diagram(diagram)
        self.assertEqual(self.series_of_tubes.moves[0], (0, 1))

    def test_continue_same_direction(self):
        self.series_of_tubes.follow_routing_diagram(diagram)
        self.assertEqual(self.series_of_tubes.moves[1], (0, 1))

    def test_collect_letters_along_the_way(self):
        self.series_of_tubes.follow_routing_diagram(diagram)
        self.assertEqual(self.series_of_tubes.letters[0], 'A')

    def test_turn_when_no_other_choice(self):
        self.series_of_tubes.follow_routing_diagram(diagram)
        self.assertEqual(self.series_of_tubes.moves[5], (1, 0))

    def test_collect_all_letters(self):
        self.series_of_tubes.follow_routing_diagram(diagram)
        self.assertEqual(str.join('', self.series_of_tubes.letters), 'ABCDEF')

    def test_puzzle_pt1(self):
        with open('Day19_puzzle.txt', 'r') as puzzle_file:
            puzzle = puzzle_file.read()
            self.series_of_tubes.follow_routing_diagram(puzzle)
            print(str.join('', self.series_of_tubes.letters))
            print(len(self.series_of_tubes.moves))
