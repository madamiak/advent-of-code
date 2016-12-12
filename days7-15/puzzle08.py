import re

width = 50
height = 6


class Puzzle08:
    def __init__(self):
        self.display = [[False for x in range(width)] for y in range(height)]
        self.rect_regex = r'rect (\d+)x(\d+)'
        self.rot_col_regex = r'rotate column x=(\d+) by (\d+)'
        self.rot_row_regex = r'rotate row y=(\d+) by (\d+)'

    def solve(self, puzzle, show_screen=False):
        for cmd in re.split('\n', puzzle):
            self.execute(cmd)
        if show_screen:
            self.show()
        return sum([sum(self.display[y]) for y in range(height)])

    def execute(self, cmd):
        if 'rect' in cmd:
            match = re.match(self.rect_regex, cmd)
            self.rect(int(match.group(1)), int(match.group(2)))
        elif 'rotate column' in cmd:
            match = re.match(self.rot_col_regex, cmd)
            self.rotate_col(int(match.group(1)), int(match.group(2)))
        elif 'rotate row' in cmd:
            match = re.match(self.rot_row_regex, cmd)
            self.rotate_row(int(match.group(1)), int(match.group(2)))

    def rect(self, x, y):
        for i in range(0, y):
            for j in range(0, x):
                self.display[i][j] = True

    def rotate_col(self, col_index, value):
        outside = []
        for i in range(height - 1, -1, -1):
            if i + value >= height:
                outside.append(self.display[i][col_index])
            else:
                self.display[i + value][col_index] = self.display[i][col_index]
        outside = outside[::-1]
        for i in range(value):
            self.display[i][col_index] = outside[i]

    def rotate_row(self, row_index, value):
        outside = []
        for i in range(width - 1, -1, -1):
            if i + value >= width:
                outside.append(self.display[row_index][i])
            else:
                self.display[row_index][i + value] = self.display[row_index][i]
        outside = outside[::-1]
        for i in range(value):
            self.display[row_index][i] = outside[i]

    def show(self):
        s = ''
        for i in range(height):
            for j in range(width):
                s += '#' if self.display[i][j] else ' '
            s += '\n'
        print s
