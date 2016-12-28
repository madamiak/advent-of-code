import hashlib


class Puzzle17:
    passing_chars = ['b', 'c', 'd', 'e', 'f']

    def __init__(self):
        pass

    @classmethod
    def candidate_moves(cls, passcode):
        moves = []
        m = hashlib.md5()
        m.update(passcode)
        hash = m.hexdigest()[:4]
        if hash[0] in cls.passing_chars:
            moves.append('U')
        if hash[1] in cls.passing_chars:
            moves.append('D')
        if hash[2] in cls.passing_chars:
            moves.append('L')
        if hash[3] in cls.passing_chars:
            moves.append('R')
        return moves

    @classmethod
    def possible_moves(cls, passcode, x, y):
        moves = cls.candidate_moves(passcode)
        if 'U' in moves and y == 0:
            moves.remove('U')
        if 'D' in moves and y == 3:
            moves.remove('D')
        if 'L' in moves and x == 0:
            moves.remove('L')
        if 'R' in moves and x == 3:
            moves.remove('R')
        return moves

    @classmethod
    def solve(cls, puzzle, x, y, part=1):
        solutions = []
        deque = []
        moves = []
        start = x, y
        end = 3, 3

        deque.append([start, moves])
        while len(deque) > 0:
            current = deque.pop(0)
            if current[0] == end:
                if part == 1:
                    return ''.join(current[1])
                else:
                    solutions.append(len(current[1]))
                    continue
            for m in cls.possible_moves(puzzle + ''.join(current[1]), current[0][0], current[0][1]):
                cur = None
                if m == 'U':
                    cur = current[0][0], current[0][1] - 1
                if m == 'D':
                    cur = current[0][0], current[0][1] + 1
                if m == 'L':
                    cur = current[0][0] - 1, current[0][1]
                if m == 'R':
                    cur = current[0][0] + 1, current[0][1]
                deque.append([cur, current[1] + [m]])
        if part == 2:
            return max(solutions)
        pass
