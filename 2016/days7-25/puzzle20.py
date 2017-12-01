import re


class Puzzle20:
    def __init__(self):
        pass

    @classmethod
    def solve(cls, puzzle, solution):
        l = sorted(map(lambda x: re.split('-', x), re.split('\n', puzzle)), key=lambda x: int(x[0]))
        i = 0
        while i < len(l) - 1:
            cur = l[i]
            nxt = l[i + 1]
            v1 = int(cur[1])
            v2 = int(nxt[0]) - 1
            v3 = int(nxt[1])
            if v1 >= v2:
                if v1 < v3:
                    l[i][1] = l[i + 1][1]
                del l[i + 1]
                continue
            if solution == 1:
                return int(l[i][1]) + 1
            i += 1
        if solution == 2:
            ips = 0
            for i in range(len(l) - 1):
                ips += int(l[i+1][0]) - int(l[i][1]) - 1
            return ips
        print l
