class InstructionExecutor(object):
    def execute(self, puzzle):
        registers = {}
        instructions = [Instruction(s) for s in str.split(puzzle, '\n')]
        max = 0
        for instruction in instructions:
            if instruction.output_register not in registers.keys():
                registers[instruction.output_register] = 0
            if instruction.condition_register not in registers.keys():
                registers[instruction.condition_register] = 0
            if instruction.meets_condition(registers[instruction.condition_register]):
                registers[instruction.output_register] += instruction.output_value()
                if registers[instruction.output_register] > max:
                    max = registers[instruction.output_register]
        registers = (sorted(registers.items(), key=lambda x: x[1]))
        return registers[-1][1], max


class Instruction(object):
    def __init__(self, instruction) -> None:
        tokens = instruction.split()
        self.output_register = tokens[0]
        self.action = tokens[1]
        self.value = int(tokens[2])
        self.condition_register = tokens[4]
        self.condition_type = tokens[5]
        self.condition_value = int(tokens[6])

    def meets_condition(self, value):
        if self.condition_type == '>':
            return value > self.condition_value
        elif self.condition_type == '>=':
            return value >= self.condition_value
        elif self.condition_type == '<=':
            return value <= self.condition_value
        elif self.condition_type == '<':
            return value < self.condition_value
        elif self.condition_type == '==':
            return value == self.condition_value
        elif self.condition_type == '!=':
            return value != self.condition_value

    def output_value(self):
        if self.action == 'inc':
            return self.value
        elif self.action == 'dec':
            return -self.value
