import re


class Puzzle15:
    discs = {}

    def __init__(self):
        pass

    @classmethod
    def solve(cls, puzzle):
        for disc in re.split('\n', puzzle):
            search = re.search(r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).', disc)
            d_num = int(search.group(1))
            d_p_pos = int(search.group(2))
            d_c_pos = int(search.group(3))
            cls.discs[d_num] = [d_c_pos, d_p_pos]
        time = 0
        while True:
            time += 1
            a = [(cls.discs[disc][0] + disc + time) % cls.discs[disc][1] for disc in cls.discs.keys()]
            r = [x == a[0] for x in a]
            if all(r):
                print a
                return time
        pass
