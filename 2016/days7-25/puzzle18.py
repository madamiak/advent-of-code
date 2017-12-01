class Puzzle18:
    def __init__(self):
        self.rules = ['^^.', '.^^', '^..', '..^']
        self.rows = []

    def solve(self, puzzle, size):
        self.rows.append(puzzle)
        while len(self.rows) < size:
            next_row = self.generate_next()
            self.rows.append(next_row)
        return reduce(lambda x, i: x+1 if i == '.' else x, [item for sublist in self.rows for item in sublist], 0)

    def get_row(self, index):
        return self.rows[index]

    def generate_next(self):
        next_row = ''
        prev_row = self.rows[-1]
        for i in range(len(prev_row)):
            neighbours = self.get_neighbours(i)
            r = [rule == neighbours for rule in self.rules]
            if any(r):
                next_row += '^'
            else:
                next_row += '.'
        return next_row

    def get_neighbours(self, i):
        prev_row = self.rows[-1]
        if i == 0:
            neighbours = '.' + ''.join(prev_row[:i+2])
        elif i == len(prev_row) - 1:
            neighbours = ''.join(prev_row[i-1:]) + '.'
        else:
            neighbours = ''.join(prev_row[i-1:i+2])
        return neighbours
