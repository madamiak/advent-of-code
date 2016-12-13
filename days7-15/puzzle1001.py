import re


class Puzzle1001:
    def __init__(self, search_pair):
        self.search_pair = search_pair
        self.bots = {}
        self.outputs = {}
        self.value_dist_regex = r'value (\d+) goes to bot (\d+)'
        self.bot_obtains_regex = r'bot (\d+) gives (low|high) to bot (\d+) and (high|low) to bot (\d+)'
        self.output_obtains_regex = r'bot (\d+) gives (low|high) to output (\d+) and (high|low) to output (\d+)'

    def solve(self, puzzle):
        # regex = re.compile(self.value_dist_regex)
        instructions = re.split('\n', puzzle)
        while len(instructions) > 0:
            action_taken = False
            for instruction in instructions[:]:
                if re.search(self.value_dist_regex, instruction) is not None:
                    action_taken = True
                    match = re.search(self.value_dist_regex, instruction)
                    value = int(match.group(1))
                    bot_number = int(match.group(2))
                    if self.bots.__contains__(bot_number):
                        self.bots[bot_number].append(value)
                    else:
                        self.bots[bot_number] = [value]
                elif re.search(self.bot_obtains_regex, instruction) is not None:
                    action_taken = True
                    match = re.search(self.bot_obtains_regex, instruction)
                    source_bot = int(match.group(1))
                    if len(self.bots[source_bot]) == 2:
                        source_bot_values = sorted(self.bots[source_bot])
                        if self.search_pair is not None:
                            if self.search_pair == source_bot_values:
                                return source_bot
                        dest_bot1 = [match.group(2), int(match.group(3))]
                        dest_bot2 = [match.group(4), int(match.group(5))]
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

                elif re.search(self.output_obtains_regex, instruction) is not None:
                    action_taken = True
                    match = re.search(self.output_obtains_regex, instruction)
                    source_bot = int(match.group(1))
                    if len(self.bots[source_bot]) == 2:
                        source_bot_values = sorted(self.bots[source_bot])
                        if self.search_pair is not None:
                            if self.search_pair == source_bot_values:
                                return source_bot
                        dest_bot1 = [match.group(2), int(match.group(3))]
                        dest_bot2 = [match.group(4), int(match.group(5))]
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

                if action_taken:
                    instructions.remove(instruction)
            if not action_taken:
                instructions = []
        pass

    def get_bot_with_values(self, values):
        return {k: v for k, v in self.bots.iteritems() if v == values or v[::-1] == values}.keys()

    def get_bot_values(self, bot_number):
        return self.bots.get(bot_number)

    def get_output_values(self, output_number):
        return self.outputs.get(output_number)
