def part_1_jump(jump):
    return 1


def part_2_jump(jump):
    return 1 if jump < 3 else -1


class MazeJumper(object):
    def count_jumps(self, puzzle, jump_function):
        jumps = [int(i) for i in puzzle.split()]
        index = 0
        steps = 0
        while 0 <= index < len(jumps):
            jump = jumps[index]
            jumps[index] += jump_function(jump)
            index += jump
            steps += 1
        return steps
