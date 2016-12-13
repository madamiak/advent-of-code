import re


class Puzzle1001:
    def __init__(self):
        self.bots = {}
        self.value_dist_regex = r'value (\d+) goes to bot (\d+)'
        self.bot_gives_regex = r'value (\d+) goes to bot (\d+)'
        pass

    def solve(self, puzzle):
        regex = re.compile(self.value_dist_regex)
        instructions = re.split('\n', puzzle)
        if regex.search(puzzle) is not None:
            match = regex.search(puzzle)
            value = [int(match.group(1))]
            bot_number = int(match.group(2))
            self.bots[bot_number] = value
        pass

    def get_bot_with_values(self, values):
        return {k: v for k, v in self.bots.iteritems() if v[0] == values[0]}.keys()[0]

    def get_bot_values(self, bot_number):
        return self.bots.get(bot_number)
