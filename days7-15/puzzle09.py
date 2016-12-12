import re


class Puzzle09:
    def __init__(self):
        pass

    @staticmethod
    def solve(puzzle, solution_1=True):
        marker_regex = re.compile(r'\((\d+)x(\d+)\)')
        if marker_regex.search(puzzle) is None:
            return len(puzzle)
        index = 0
        res = str(puzzle)
        while marker_regex.search(res) is not None:
            marker = marker_regex.search(res)
            letters = int(marker.group(1))
            times = int(marker.group(2))
            if solution_1:
                index += marker.start(0) + len(res[marker.end(0):marker.end(0) + letters]) * times
            else:
                index += marker.start(0) + Puzzle09.solve(res[marker.end(0):marker.end(0) + letters], solution_1=False) * times
            res = res[marker.end(0) + letters:]
        index += len(res)
        return index
