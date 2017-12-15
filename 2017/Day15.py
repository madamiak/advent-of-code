class DuelingGenerators(object):
    def __init__(self, fac_a, fac_b) -> None:
        self.fac_a = fac_a
        self.fac_b = fac_b

    def matches(self, puzzle, pairs, divs=(1, 1)):
        gen_a = int(str.split(puzzle, '\n')[0].split()[-1])
        gen_b = int(str.split(puzzle, '\n')[1].split()[-1])
        matches = 0
        for _ in range(pairs):
            gen_a = self._next_value(gen_a, self.fac_a, divs[0])
            gen_b = self._next_value(gen_b, self.fac_b, divs[1])
            bin_a = bin(gen_a)[-16:]
            bin_b = bin(gen_b)[-16:]
            if bin_a == bin_b:
                matches += 1
        return matches

    def _next_value(self, gen, fac, div):
        gen = (gen * fac) % 2147483647
        while gen % div != 0:
            gen = (gen * fac) % 2147483647
        return gen
