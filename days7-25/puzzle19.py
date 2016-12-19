import copy


class Puzzle19:
    def __init__(self):
        pass

    @classmethod
    def solve_1(cls, puzzle):
        elves = [x for x in range(int(puzzle))]
        while True:
            new_elves = copy.deepcopy(elves)
            for i in range(len(elves)):
                if i % 2 == 1:
                    new_elves[i] = -1
            new_elves = filter(lambda y: y != -1, new_elves)
            if len(new_elves) == 1:
                return new_elves[0] + 1
            if len(elves) % 2 == 1:
                elves = [new_elves[-1]] + new_elves[:-1]
            else:
                elves = new_elves

    @classmethod
    def solve_2(cls, puzzle):
        elves = [[(x - 1) % puzzle, (x + 1) % puzzle, x] for x in range(int(puzzle))]
        result = elves[0][2]
        across = elves[puzzle / 2]
        for i in range(puzzle - 1):
            elves[across[0]][1] = elves[across[2]][1]
            elves[across[1]][0] = elves[across[2]][0]
            rem = across[2]
            across = elves[across[1]]
            if (puzzle - i) % 2 == 1:
                across = elves[across[1]]
            result = elves[result][1]
            elves[rem] = None
        return result + 1
