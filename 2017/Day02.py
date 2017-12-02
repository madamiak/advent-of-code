class ChecksumCalculator(object):
    def calculate_1(self, grid):
        result = 0
        rows = list(map(lambda row: row.split(), str.split(grid, '\n')))
        for row in rows:
            row = sorted(list(map(lambda s: int(s), row)))
            result += row[-1] - row[0]
        return result

    def calculate_2(self, grid):
        result = 0
        rows = list(map(lambda row: row.split(), str.split(grid, '\n')))
        for row in rows:
            row = sorted(list(map(lambda s: int(s), row)), reverse=True)
            for index, number in enumerate(row[:-1]):
                for other_number in row[index+1:]:
                    if number % other_number == 0:
                        result += number / other_number
        return result
