import re


class Puzzle21:
    def __init__(self):
        pass

    @classmethod
    def swap_position(cls, word, pos_x, pos_y):
        word = list(word)
        word[pos_x], word[pos_y] = word[pos_y], word[pos_x]
        return ''.join(word)

    @classmethod
    def swap_letter(cls, word, let_1, let_2):
        word = list(word)
        pos_x = word.index(let_1)
        pos_y = word.index(let_2)
        word[pos_x], word[pos_y] = word[pos_y], word[pos_x]
        return ''.join(word)

    @classmethod
    def reverse_positions(cls, word, start, stop):
        word = list(word[:start] + word[start:stop + 1][::-1] + word[stop + 1:])
        return ''.join(word)

    @classmethod
    def rotate(cls, word, direction, steps):
        steps *= -1 if direction == 'right' else 1
        word = list(word[steps:] + word[:steps])
        return ''.join(word)

    @classmethod
    def move(cls, word, pos_x, pos_y):
        word = list(word)
        if pos_x < pos_y:
            word.insert(pos_y + 1, word[pos_x])
            del word[pos_x]
        else:
            word.insert(pos_y, word[pos_x])
            del word[pos_x + 1]
        return ''.join(word)

    @classmethod
    def rotate_on_letter(cls, word, let):
        word = list(word)
        pos = word.index(let)
        for i in range(pos + 1):
            word = cls.rotate(word, 'right', 1)
        if pos >= 4:
            word = cls.rotate(word, 'right', 1)
        return ''.join(word)

    @classmethod
    def reverse_rotate_on_letter(cls, word, let):
        word = list(word)
        pos = word.index(let)
        reverse = {
            0: 7,
            1: 7,
            2: 2,
            3: 6,
            4: 1,
            5: 5,
            6: 0,
            7: 4
        }
        word = cls.rotate(word, 'right', reverse.get(pos))
        return ''.join(word)

    @classmethod
    def solve_1(cls, puzzle, word):
        i = 0
        for instruction in re.split('\n', puzzle):
            print i, ' ', instruction, ' ', word
            i += 1
            if re.search(r'swap position (\d+) with position (\d+)', instruction) is not None:
                search = re.search(r'swap position (\d+) with position (\d+)', instruction)
                word = cls.swap_position(word, int(search.group(1)), int(search.group(2)))
            elif re.search(r'swap letter ([a-z]) with letter ([a-z])', instruction) is not None:
                search = re.search(r'swap letter ([a-z]) with letter ([a-z])', instruction)
                word = cls.swap_letter(word, search.group(1), search.group(2))
            elif re.search(r'reverse positions (\d+) through (\d+)', instruction) is not None:
                search = re.search(r'reverse positions (\d+) through (\d+)', instruction)
                word = cls.reverse_positions(word, int(search.group(1)), int(search.group(2)))
            elif re.search(r'rotate (left|right) (\d+) step', instruction) is not None:
                search = re.search(r'rotate (left|right) (\d+) step', instruction)
                word = cls.rotate(word, search.group(1), int(search.group(2)))
            elif re.search(r'move position (\d+) to position (\d+)', instruction) is not None:
                search = re.search(r'move position (\d+) to position (\d+)', instruction)
                word = cls.move(word, int(search.group(1)), int(search.group(2)))
            elif re.search(r'rotate based on position of letter ([a-z])', instruction) is not None:
                search = re.search(r'rotate based on position of letter ([a-z])', instruction)
                word = cls.rotate_on_letter(word, search.group(1))
        return word

    @classmethod
    def solve_2(cls, puzzle, word):
        i = 0
        for instruction in reversed(re.split('\n', puzzle)):
            if i == 11:
                pass
            print i, ' ', instruction, ' ', word
            i += 1
            if re.search(r'swap position (\d+) with position (\d+)', instruction) is not None:
                search = re.search(r'swap position (\d+) with position (\d+)', instruction)
                word = cls.swap_position(word, int(search.group(2)), int(search.group(1)))
            elif re.search(r'swap letter ([a-z]) with letter ([a-z])', instruction) is not None:
                search = re.search(r'swap letter ([a-z]) with letter ([a-z])', instruction)
                word = cls.swap_letter(word, search.group(2), search.group(1))
            elif re.search(r'reverse positions (\d+) through (\d+)', instruction) is not None:
                search = re.search(r'reverse positions (\d+) through (\d+)', instruction)
                word = cls.reverse_positions(word, int(search.group(1)), int(search.group(2)))
            elif re.search(r'rotate (left|right) (\d+) step', instruction) is not None:
                search = re.search(r'rotate (left|right) (\d+) step', instruction)
                word = cls.rotate(word, 'left' if 'right' == search.group(1) else 'right', int(search.group(2)))
            elif re.search(r'move position (\d+) to position (\d+)', instruction) is not None:
                search = re.search(r'move position (\d+) to position (\d+)', instruction)
                word = cls.move(word, int(search.group(2)), int(search.group(1)))
            elif re.search(r'rotate based on position of letter ([a-z])', instruction) is not None:
                search = re.search(r'rotate based on position of letter ([a-z])', instruction)
                word = cls.reverse_rotate_on_letter(word, search.group(1))
        return word
