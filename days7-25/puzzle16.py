class Puzzle16:
    def __init__(self):
        pass

    def generate_random_data(self, puzzle):
        return str(puzzle + '0' + ''.join(['0' if x == '1' else '1' for x in reversed(puzzle)]))

    def generate_checksum(self, data):
        checksum = data
        while len(checksum) % 2 == 0:
            checksum = ['1' if checksum[i] == checksum[i+1] else '0' for i in range(0, len(checksum)-1, 2)]
        return ''.join(checksum)

    def solve(self, disk_size, puzzle):
        a = puzzle
        while len(a) < disk_size:
            a = self.generate_random_data(a)
        return self.generate_checksum(a[:disk_size])
