import math

moves = {
    'n': (0, 1, -1),
    's': (0, -1, 1),
    'ne': (1, 0, -1),
    'sw': (-1, 0, 1),
    'nw': (-1, 1, 0),
    'se': (1, -1, 0),
}


class HexEd(object):
    def count_steps(self, puzzle):
        steps = str.split(puzzle, ',')
        x, y, z = 0, 0, 0
        current_distance = 0
        max_distance = 0
        for step in steps:
            x += moves[step][0]
            y += moves[step][1]
            z += moves[step][2]
            current_distance = self._distance(x, y, z)
            if current_distance > max_distance:
                max_distance = current_distance
        return current_distance, max_distance

    def _distance(self, x, y, z):
        return int((math.fabs(x) + math.fabs(y) + math.fabs(z)) / 2)
