import re


class Puzzle23:
    def __init__(self, registers={'a': 0, 'b': 0, 'c': 0, 'd': 0}):
        self.registers = registers

    def solve(self, puzzle):
        instructions = re.split("\n", puzzle)
        i = 0
        while i < len(instructions):
            print str(i), ' ', instructions[i], ' ', self.registers
            if re.search(r'cpy (-\d+|\d+) (a|b|c|d)', instructions[i]) is not None:
                search = re.search(r'cpy (-\d+|\d+) (a|b|c|d)', instructions[i])
                value = int(search.group(1))
                register = search.group(2)
                self.registers[register] = value
            elif re.search(r'cpy (a|b|c|d) (a|b|c|d)', instructions[i]) is not None:
                search = re.search(r'cpy (a|b|c|d) (a|b|c|d)', instructions[i])
                src_reg = search.group(1)
                dst_reg = search.group(2)
                if instructions[i + 1].startswith('inc') and \
                        instructions[i + 2].startswith('dec') and \
                        instructions[i + 3].startswith('jnz') and \
                        instructions[i + 4].startswith('dec') and \
                        instructions[i + 5].startswith('jnz'):
                    reg_res = re.search(r'inc (a|b|c|d)', instructions[i + 1]).group(1)
                    reg_mul_1 = src_reg
                    reg_mul_2 = re.search(r'dec (a|b|c|d)', instructions[i + 4]).group(1)
                    reg_z = re.search(r'dec (a|b|c|d)', instructions[i + 2]).group(1)
                    self.registers[reg_res] = self.registers[reg_mul_1] * self.registers[reg_mul_2]
                    self.registers[reg_mul_2] = 0
                    self.registers[reg_z] = 0
                    i += 6
                    continue
                else:
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
                    i += value_2
                    continue
            elif re.search(r'jnz (a|b|c|d) (-\d+|\d+)', instructions[i]) is not None:
                search = re.search(r'jnz (a|b|c|d) (-\d+|\d+)', instructions[i])
                register = search.group(1)
                value = int(search.group(2))
                if self.registers[register] != 0:
                    i += value
                    continue
            elif re.search(r'jnz (-\d+|\d+) (a|b|c|d)', instructions[i]) is not None:
                search = re.search(r'jnz (-\d+|\d+) (a|b|c|d)', instructions[i])
                value = int(search.group(1))
                register = search.group(2)
                if value != 0:
                    i += self.registers[register]
                    continue
            elif re.search(r'tgl (a|b|c|d)', instructions[i]) is not None:
                search = re.search(r'tgl (a|b|c|d)', instructions[i])
                register = search.group(1)
                instruction = i + self.registers[register]
                if instruction in range(len(instructions)):
                    if 'inc' in instructions[instruction]:
                        instructions[instruction] = instructions[instruction].replace('inc', 'dec')
                    elif 'jnz' in instructions[instruction]:
                        instructions[instruction] = instructions[instruction].replace('jnz', 'cpy')
                    elif 'cpy' in instructions[instruction]:
                        instructions[instruction] = instructions[instruction].replace('cpy', 'jnz')
                    else:
                        instructions[instruction] = re.sub(r'dec|tgl', 'inc', instructions[instruction])
            i += 1
        pass

    def get_register(self, register_name):
        return self.registers[register_name]
        pass
