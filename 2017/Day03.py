import math

right, up, left, down = (1, 0), (0, -1), (-1, 0), (0, 1)
turn = {right: up, up: left, left: down, down: right}
adjacencies = {(1, 1), (0, 1), (-1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)}


class Spiral(object):
    def distance(self, number):
        size = int(math.ceil(math.sqrt(int(number))))
        size = size if size % 2 != 0 else size + 1
        cur_x, cur_y = size // 2, size // 2
        next_x, next_y = down
        square = [[None] * size for _ in range(size)]
        cells = size * size
        position = (0, 0)
        for index in range(cells):
            square[cur_y][cur_x] = index + 1
            if square[cur_y][cur_x] == int(number):
                position = (cur_x, cur_y)
                break
            turn_x, turn_y = turn[next_x, next_y]
            new_x, new_y = cur_x + turn_x, cur_y + turn_y
            if 0 <= new_y < size and 0 <= new_x < size and square[new_y][new_x] is None:
                cur_x, cur_y = new_x, new_y
                next_x, next_y = turn_x, turn_y
            else:
                cur_x, cur_y = cur_x + next_x, cur_y + next_y
        return int(math.fabs(position[0] - size // 2) + math.fabs(position[1] - size // 2))

    def value(self, limit):
        size = int(math.ceil(math.sqrt(int(limit))))
        size = size if size % 2 != 0 else size + 1
        cur_x, cur_y = size // 2, size // 2
        next_x, next_y = down
        square = [[None] * size for _ in range(size)]
        cells = size * size
        result = 0
        for index in range(cells):
            if index == 0:
                square[cur_y][cur_x] = 1
            else:
                square[cur_y][cur_x] = 0
                for adjacency in adjacencies:
                    adj_x, adj_y = adjacency
                    new_x, new_y = cur_x + adj_x, cur_y + adj_y
                    if 0 <= new_x < size and 0 <= new_y < size and square[new_y][new_x] is not None:
                        square[cur_y][cur_x] += square[new_y][new_x]
            if int(square[cur_y][cur_x]) > int(limit):
                result = int(square[cur_y][cur_x])
                break
            turn_x, turn_y = turn[next_x, next_y]
            new_x, new_y = cur_x + turn_x, cur_y + turn_y
            if 0 <= new_y < size and 0 <= new_x < size and square[new_y][new_x] is None:
                cur_x, cur_y = new_x, new_y
                next_x, next_y = turn_x, turn_y
            else:
                cur_x, cur_y = cur_x + next_x, cur_y + next_y
        return result
