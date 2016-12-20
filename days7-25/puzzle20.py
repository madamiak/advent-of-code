import re


class Puzzle20:
    def __init__(self):
        pass

    @classmethod
    def solve(cls, puzzle):
        l = sorted(map(lambda x: re.split('-', x), re.split('\n', puzzle)), key=lambda x: x[0])
        print l
        return int(l[0][1])+1
