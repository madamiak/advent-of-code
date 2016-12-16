import re


class Puzzle10:
    def __init__(self):
        self.bots = {}
        self.value_dist_regex = r'value (\d+) goes to (bot \d+|output \d+)'
        self.bot_obtains_regex = r'(bot \d+) gives (low|high) to (bot \d+|output \d+) ' \
                                 r'and (high|low) to (bot \d+|output \d+)'

    def solve(self, puzzle, search_pair=None):
        instructions = re.split('\n', puzzle)
        while len(instructions) > 0:
            action_taken = False
            for instruction in instructions[:]:
                if re.search(self.value_dist_regex, instruction) is not None:
                    match = re.search(self.value_dist_regex, instruction)
                    value = int(match.group(1))
                    bot = match.group(2)
                    if self.bots.__contains__(bot):
                        self.bots[bot].append(value)
                    else:
                        self.bots[bot] = [value]
                    action_taken = True
                    instructions.remove(instruction)
                elif re.search(self.bot_obtains_regex, instruction) is not None:
                    match = re.search(self.bot_obtains_regex, instruction)
                    source_bot = match.group(1)
                    if not self.bots.__contains__(source_bot):
                        continue
                    if len(self.bots[source_bot]) == 2:
                        source_bot_values = sorted(self.bots[source_bot])
                        if search_pair is not None:
                            if search_pair == source_bot_values:
                                return source_bot
                        dest_bot1 = [match.group(2), match.group(3)]
                        dest_bot2 = [match.group(4), match.group(5)]
                        if dest_bot1[0] == 'high':
                            if self.bots.__contains__(dest_bot1[1]):
                                self.bots[dest_bot1[1]].append(source_bot_values[1])
                            else:
                                self.bots[dest_bot1[1]] = [source_bot_values[1]]
                        else:
                            if self.bots.__contains__(dest_bot1[1]):
                                self.bots[dest_bot1[1]].append(source_bot_values[0])
                            else:
                                self.bots[dest_bot1[1]] = [source_bot_values[0]]
                        if dest_bot2[0] == 'high':
                            if self.bots.__contains__(dest_bot2[1]):
                                self.bots[dest_bot2[1]].append(source_bot_values[1])
                            else:
                                self.bots[dest_bot2[1]] = [source_bot_values[1]]
                        else:
                            if self.bots.__contains__(dest_bot2[1]):
                                self.bots[dest_bot2[1]].append(source_bot_values[0])
                            else:
                                self.bots[dest_bot2[1]] = [source_bot_values[0]]
                        self.bots[source_bot] = []
                        action_taken = True
                        instructions.remove(instruction)
            if not action_taken:
                instructions = []
        pass

    def get_bot_with_values(self, values):
        return {k: v for k, v in self.bots.iteritems() if v == values or v[::-1] == values}.keys()

    def get_bot_values(self, bot_number):
        return self.bots.get(bot_number)
