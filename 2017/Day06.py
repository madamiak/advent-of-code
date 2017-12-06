class BankBalancer(object):
    def count_cycles(self, puzzle):
        banks = [int(i) for i in str.split(puzzle, '\t')]
        sequences = []
        cycles = 0
        while True:
            cycles += 1
            value, index = self._max(banks)
            banks[index] = 0
            index += 1
            for i in range(value):
                banks[(index + i) % len(banks)] += 1
            if banks in sequences:
                break
            else:
                sequences.append(banks[::])
        return cycles, cycles - (len(sequences) - sequences[::-1].index(banks))

    def _max(self, array):
        maximum = max(array)
        return int(maximum), array.index(maximum)
