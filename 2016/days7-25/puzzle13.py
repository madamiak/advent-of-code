class Puzzle13:
    def __init__(self):
        pass

    @classmethod
    def solve(cls, m_x, m_y, a_x, a_y, num, part=1):
        grid = []
        for y in range(m_y + 1):
            row = []
            for x in range(m_x + 1):
                if x == a_x and y == a_y:
                    row.append('G')
                else:
                    b = str(bin(x * x + 3 * x + 2 * x * y + y + y * y + num))[2:]
                    sum = reduce(lambda i, s: i + 1 if s == '1' else i, b[:], 0)
                    if sum % 2 == 0:
                        row.append('.')
                    else:
                        row.append('#')
            grid.append(row)
        print '\n'.join(''.join(s) for s in grid)

        start = [1, 1, []]
        stack = []
        visited = [[start[0], start[1]]]
        steps = 0

        print
        print

        stack.append(start)
        while len(stack) > 0:
            current = stack.pop()
            steps += 1
            if part == 1 and grid[current[1]][current[0]] == 'G':
                for c in current[2]:
                    grid[c[1]][c[0]] = 'X'
                print '\n'.join(''.join(s) for s in grid)
                return len(current[2])
            if part == 2 and len(current[2]) > 50:
                return len(visited)

            for m in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                if current[0] + m[0] >= 0 and current[1] + m[1] >= 0:
                    if [current[0] + m[0], current[1] + m[1]] not in visited:
                        if grid[current[1] + m[1]][current[0] + m[0]] != '#':
                            visited.append([current[0] + m[0], current[1] + m[1]])
                            stack.append(
                                [current[0] + m[0], current[1] + m[1], current[2] + [[current[0], current[1]]]])
