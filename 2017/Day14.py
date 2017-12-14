from Day10 import part2_convert, part2_result


class DiskDefragmentation(object):
    def __init__(self, knot_hasher) -> None:
        self.knot_hasher = knot_hasher

    def defragment(self, puzzle):
        ones = 0
        squares = []
        for i in range(128):
            text = puzzle + "-" + str(i)
            hexadecimal = self.knot_hasher.hash(256, text, part2_convert, 64, part2_result)
            binary = '{:04b}'.format(int(hexadecimal, 16)).rjust(128, '0')
            row = [int(digit) for digit in binary]
            squares.append(row)
            ones += sum(row)
        groups = 0
        visited = []
        rng = range(128)
        for i, row in enumerate(squares):
            for j, column in enumerate(row):
                if squares[i][j] == 1 and (i, j) not in visited:
                    groups += 1
                    queue = [(i, j)]
                    while queue:
                        y, x = queue.pop()
                        visited.append((y, x))
                        for new_y, new_x in (y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1):
                            if new_y in rng and new_x in rng and squares[new_y][new_x] and (new_y, new_x) not in visited:
                                queue.append((new_y, new_x))
        return ones, groups
