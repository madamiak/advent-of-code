from unittest import TestCase

from puzzle21 import Puzzle21


class TestPuzzle21(TestCase):
    pass

    def test_swap_position(self):
        self.assertEqual(Puzzle21.swap_position('abcde', 4, 0), 'ebcda')

    def test_swap_position_rev(self):
        self.assertEqual(Puzzle21.swap_position('ebcda', 4, 0), 'abcde')
        self.assertEqual(Puzzle21.swap_position('ebcda', 0, 4), 'abcde')

    def test_swap_letter(self):
        self.assertEqual(Puzzle21.swap_letter('ebcda', 'd', 'b'), 'edcba')

    def test_swap_letter_rev(self):
        self.assertEqual(Puzzle21.swap_letter('edcba', 'd', 'b'), 'ebcda')
        self.assertEqual(Puzzle21.swap_letter('edcba', 'b', 'd'), 'ebcda')

    def test_reverse_positions(self):
        self.assertEqual(Puzzle21.reverse_positions('edcba', 0, 4), 'abcde')

    def test_reverse_positions_rev(self):  # !
        self.assertEqual(Puzzle21.reverse_positions('abcde', 0, 4), 'edcba')

    def test_rotate(self):
        self.assertEqual(Puzzle21.rotate('abcde', 'left', 1), 'bcdea')

    def test_rotate_rev(self):  # !
        self.assertEqual(Puzzle21.rotate('bcdea', 'right', 1), 'abcde')

    def test_move_asc(self):
        self.assertEqual(Puzzle21.move('bcdea', 1, 4), 'bdeac')

    def test_move_asc_rev(self):  # !
        self.assertEqual(Puzzle21.move('bdeac', 4, 1), 'bcdea')

    def test_move_desc(self):
        self.assertEqual(Puzzle21.move('bdeac', 3, 0), 'abdec')

    def test_move_desc_rev(self):
        self.assertEqual(Puzzle21.move('abdec', 0, 3), 'bdeac')

    def test_rotate_on_letter_small_index(self):
        self.assertEqual(Puzzle21.rotate_on_letter('abdec', 'b'), 'ecabd')

    def test_rotate_on_letter_big_index(self):
        self.assertEqual(Puzzle21.rotate_on_letter('ecabd', 'd'), 'decab')

    def test_reverse_posistions_2(self):
        self.assertEqual(Puzzle21.reverse_positions('hbcdfaeg', 4, 7), 'hbcdgeaf')

    def test_multiple_instructions(self):
        self.assertEqual(Puzzle21.solve_1('swap position 4 with position 0\n'
                                          'swap letter d with letter b\n'
                                          'reverse positions 0 through 4\n'
                                          'rotate left 1 step\n'
                                          'move position 1 to position 4\n'
                                          'move position 3 to position 0\n'
                                          'rotate based on position of letter b\n'
                                          'rotate based on position of letter d'
                                          , 'abcde'), 'decab')

    def test(self):
        with open('Puzzle21.txt') as puzzle:
            print Puzzle21.solve_1(puzzle.read(), 'abcdefgh')

    def test_reversed_rotate_on_letter(self):
        self.assertEqual(Puzzle21.reverse_rotate_on_letter(Puzzle21.rotate_on_letter('fbgdceah', 'a'), 'a'), 'fbgdceah')
        self.assertEqual(Puzzle21.reverse_rotate_on_letter(Puzzle21.rotate_on_letter('fbgdceah', 'b'), 'b'), 'fbgdceah')
        self.assertEqual(Puzzle21.reverse_rotate_on_letter(Puzzle21.rotate_on_letter('fbgdceah', 'c'), 'c'), 'fbgdceah')
        self.assertEqual(Puzzle21.reverse_rotate_on_letter(Puzzle21.rotate_on_letter('fbgdceah', 'd'), 'd'), 'fbgdceah')
        self.assertEqual(Puzzle21.reverse_rotate_on_letter(Puzzle21.rotate_on_letter('fbgdceah', 'e'), 'e'), 'fbgdceah')
        self.assertEqual(Puzzle21.reverse_rotate_on_letter(Puzzle21.rotate_on_letter('fbgdceah', 'f'), 'f'), 'fbgdceah')
        self.assertEqual(Puzzle21.reverse_rotate_on_letter(Puzzle21.rotate_on_letter('fbgdceah', 'g'), 'g'), 'fbgdceah')
        self.assertEqual(Puzzle21.reverse_rotate_on_letter(Puzzle21.rotate_on_letter('fbgdceah', 'h'), 'h'), 'fbgdceah')

    def test_2(self):
        with open('Puzzle21.txt') as puzzle:
            print Puzzle21.solve_2(puzzle.read(), 'fbgdceah')
