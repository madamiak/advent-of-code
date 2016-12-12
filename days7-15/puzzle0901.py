import re


class Puzzle0901:
    def __init__(self):
        pass

    @staticmethod
    def solve(puzzle):
        res = str(puzzle)
        index = 0
        regex = re.compile(r'\((\d)+x(\d)+\)')
        while regex.search(str(puzzle)[index:]) is not None:
            search = regex.search(res)
            close_bracket = str(res).index(')') + 1
            end_marker = close_bracket + int(search.group(1))
            index += search.start(0)
            repeat = ''
            for i in range(0, int(search.group(2)) - 1):
                repeat += res[close_bracket:end_marker]
            index += len(repeat)
            res = res.replace(search.group(0), repeat, 1)
        return index
