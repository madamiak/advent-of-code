import re


class Puzzle22:
    def __init__(self):
        pass

    @classmethod
    def solve(cls, puzzle):
        volumes = []
        viables = []
        regex = re.compile(r'/dev/grid/node-x(\d+)-y(\d+)(\s+)(\d+)T(\s+)(\d+)T(\s+)(\d+)T(\s+)(\d+)%')
        for line in re.split('\n', puzzle):
            search = regex.search(line)
            if search is not None:
                x = int(search.group(1))
                y = int(search.group(2))
                size = int(search.group(4))
                used = int(search.group(6))
                avail = int(search.group(8))
                use = int(search.group(10))
                volumes.append([x, y, size, used, avail, use])
        for v1 in volumes:
            for v2 in volumes:
                if v1[3] != 0 and v1 != v2 and v1[3] <= v2[4] and [v2[0], v2[1], v1[0], v1[1]] not in viables:
                    viables.append([v1[0], v1[1], v2[0], v2[1]])
        return len(viables)
