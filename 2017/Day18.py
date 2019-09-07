from collections import defaultdict


class Duet(object):
    def __init__(self, last_frequency=None) -> None:
        self.registers_0 = defaultdict(int)
        self.registers_1 = defaultdict(int)
        self.queue_0 = []
        self.queue_1 = []
        self.sent_1 = 0
        self.last_frequency = last_frequency

    def parallel(self, puzzle):
        instructions = [s.split() for s in str.split(puzzle, '\n')]
        indexes = [0, 0]
        registers = [self.registers_0, self.registers_1]
        self.registers_0['p'] = 0
        self.registers_1['p'] = 1
        queues = [self.queue_0, self.queue_1]
        waiting = [False, False]
        i = 0
        while not all(waiting):
            while True:
                instruction = instructions[indexes[i]]
                print('program: ', i, instruction, self.registers_0 if i == 0 else self.registers_1)
                if instruction[0] == 'set':
                    try:
                        instruction[2] = int(instruction[2])
                    except ValueError:
                        pass
                    indexes[i] += self.set(instruction[1], instruction[2], registers[i])
                elif instruction[0] == 'add':
                    try:
                        instruction[2] = int(instruction[2])
                    except ValueError:
                        pass
                    indexes[i] += self.add(instruction[1], instruction[2], registers[i])
                elif instruction[0] == 'mul':
                    try:
                        instruction[2] = int(instruction[2])
                    except ValueError:
                        pass
                    indexes[i] += self.mul(instruction[1], instruction[2], registers[i])
                elif instruction[0] == 'mod':
                    try:
                        instruction[2] = int(instruction[2])
                    except ValueError:
                        pass
                    indexes[i] += self.mod(instruction[1], instruction[2], registers[i])
                elif instruction[0] == 'jgz':
                    try:
                        instruction[1] = int(instruction[1])
                    except ValueError:
                        pass
                    try:
                        instruction[2] = int(instruction[2])
                    except ValueError:
                        pass
                    indexes[i] += self.jgz(instruction[1], instruction[2], registers[i])
                elif instruction[0] == 'snd':
                    if i == 1:
                        self.sent_1 += 1
                    try:
                        instruction[1] = int(instruction[1])
                    except ValueError:
                        pass
                    indexes[i] += self.send(instruction[1], queues[(i + 1) % 2], registers[i])
                elif instruction[0] == 'rcv':
                    if len(queues[i]) == 0:
                        waiting[i] = True
                        i = (i + 1) % 2
                        waiting[i] = len(self.queue_0 if i == 0 else self.queue_1) == 0
                        break
                    else:
                        indexes[i] += self.receive(instruction[1], queues[i], registers[i])

    def execute(self, puzzle):
        instructions = [s.split() for s in str.split(puzzle, '\n')]
        index = 0
        while True:
            instruction = instructions[index]
            print(instruction)
            if instruction[0] == 'set':
                try:
                    instruction[2] = int(instruction[2])
                except ValueError:
                    pass
                index += self.set(instruction[1], instruction[2], self.registers_0)
            elif instruction[0] == 'add':
                try:
                    instruction[2] = int(instruction[2])
                except ValueError:
                    pass
                index += self.add(instruction[1], instruction[2], self.registers_0)
            elif instruction[0] == 'mul':
                try:
                    instruction[2] = int(instruction[2])
                except ValueError:
                    pass
                index += self.mul(instruction[1], instruction[2], self.registers_0)
            elif instruction[0] == 'mod':
                try:
                    instruction[2] = int(instruction[2])
                except ValueError:
                    pass
                index += self.mod(instruction[1], instruction[2], self.registers_0)
            elif instruction[0] == 'jgz':
                try:
                    instruction[2] = int(instruction[2])
                except ValueError:
                    pass
                index += self.jgz(instruction[1], instruction[2], self.registers_0)
            elif instruction[0] == 'snd':
                index += self.snd(instruction[1], self.registers_0)
            elif instruction[0] == 'rcv':
                result = self.rcv(instruction[1], self.registers_0)
                if result[1]:
                    return
                index += result[0]

    def initialize_register(self, register, registers):
        if isinstance(register, str) and register not in registers.keys():
            registers[register] = 0

    def set(self, register, value, registers):
        self.initialize_register(value, registers)
        self.initialize_register(register, registers)
        if value in registers.keys():
            registers[register] = registers[value]
        else:
            registers[register] = value
        return 1

    def add(self, register, value, registers):
        self.initialize_register(value, registers)
        self.initialize_register(register, registers)
        if value in registers.keys():
            registers[register] = registers[register] + registers[value]
        else:
            registers[register] = registers[register] + value
        return 1

    def mul(self, register, value, registers):
        self.initialize_register(value, registers)
        self.initialize_register(register, registers)
        if value in registers.keys():
            registers[register] = registers[register] * registers[value]
        else:
            registers[register] = registers[register] * value
        return 1

    def mod(self, register, value, registers):
        self.initialize_register(value, registers)
        self.initialize_register(register, registers)
        if value in registers.keys():
            registers[register] = registers[register] % registers[value]
        else:
            registers[register] = registers[register] % value
        return 1

    def snd(self, register, registers):
        self.initialize_register(register, registers)
        self.last_frequency = registers[register]
        return 1

    def rcv(self, register, registers):
        self.initialize_register(register, registers)
        if registers[register] != 0:
            registers[register] = self.last_frequency
            return 1, True
        return 1, False

    def jgz(self, register, value, registers):
        self.initialize_register(value, registers)
        self.initialize_register(register, registers)
        if isinstance(register, int):
            if int(register) > 0:
                if value in registers.keys():
                    return registers[value]
                else:
                    return value

        if registers[register] > 0:
            if value in registers.keys():
                return registers[value]
            else:
                return value
        else:
            return 1

    def send(self, value, queue, registers):
        self.initialize_register(value, registers)
        if value in registers.keys():
            queue.insert(0, registers[value])
        else:
            queue.insert(0, value)
        return 1

    def receive(self, register, queue, registers):
        registers[register] = queue.pop()
        return 1
