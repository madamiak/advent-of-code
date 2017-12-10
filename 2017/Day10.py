def part1_convert(puzzle):
    return [int(length) for length in str.split(puzzle, ',')]


def part1_result(numbers):
    return numbers[0] * numbers[1]


def part2_convert(puzzle):
    return [ord(sign) for sign in puzzle] + [17, 31, 73, 47, 23]


def part2_result(numbers):
    block_size = 16
    current_position = 0
    results = []
    hash = ''
    for _ in range(int(len(numbers) / block_size)):
        to_xor = numbers[current_position:current_position + block_size]
        result = to_xor[0]
        for number in to_xor[1:]:
            result ^= number
        results.append(result)
        current_position += block_size
    for number in results:
        hash += hex(number)[2:].rjust(2, '0')
    return hash


class KnotHash(object):
    def hash(self, list_size, puzzle, converting_function, rounds, resulting_function):
        numbers = list(range(list_size))
        lengths = converting_function(puzzle)
        current_position = 0
        skip_size = 0
        for _ in range(rounds):
            for length in lengths:
                start_index = current_position % len(numbers)
                end_index = (current_position + length) % len(numbers)
                if start_index <= end_index:
                    reversed_numbers = list(reversed(numbers[start_index:end_index]))
                else:
                    reversed_numbers = list(reversed(numbers[start_index:] + numbers[:end_index]))
                for reversed_index, reversed_value in enumerate(reversed_numbers):
                    numbers[(start_index + reversed_index) % len(numbers)] = reversed_value
                current_position += length + skip_size
                skip_size += 1
        return resulting_function(numbers)
