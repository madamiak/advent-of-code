import re


class Puzzle12:
    def __init__(self):
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

    def solve(self, puzzle):
        instructions = re.split("\n", puzzle)
        i = 0
        while i < len(instructions):
            print str(i), ' ', instructions[i]
            if re.search(r'cpy (\d+) (a|b|c|d)', instructions[i]) is not None:
                search = re.search(r'cpy (\d+) (a|b|c|d)', instructions[i])
                value = int(search.group(1))
                register = search.group(2)
                self.registers[register] = value
            elif re.search(r'cpy (a|b|c|d) (a|b|c|d)', instructions[i]) is not None:
                search = re.search(r'cpy (a|b|c|d) (a|b|c|d)', instructions[i])
                src_reg = search.group(1)
                dst_reg = search.group(2)
                self.registers[dst_reg] = self.registers[src_reg]
            elif re.search(r'inc (a|b|c|d)', instructions[i]) is not None:
                search = re.search(r'inc (a|b|c|d)', instructions[i])
                register = search.group(1)
                self.registers[register] += 1
            elif re.search(r'dec (a|b|c|d)', instructions[i]) is not None:
                search = re.search(r'dec (a|b|c|d)', instructions[i])
                register = search.group(1)
                self.registers[register] -= 1
            elif re.search(r'jnz (-\d+|\d+) (-\d+|\d+)', instructions[i]) is not None:
                search = re.search(r'jnz (-\d+|\d+) (-\d+|\d+)', instructions[i])
                value_1 = int(search.group(1))
                value_2 = int(search.group(2))
                if value_1 != 0:
                    i += value_2 if value_2 < 0 else value_2 + 1
                    continue
            elif re.search(r'jnz (a|b|c|d) (-\d+|\d+)', instructions[i]) is not None:
                search = re.search(r'jnz (a|b|c|d) (-\d+|\d+)', instructions[i])
                register = search.group(1)
                value = int(search.group(2))
                if self.registers[register] != 0:
                    i += value if value < 0 else value + 1
                    continue
            i += 1
        pass

    def get_register(self, register_name):
        return self.registers[register_name]
        pass
