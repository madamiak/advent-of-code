class SeriesOfTubes:
    def __init__(self):
        self.moves = []
        self.cur_pos = (0, 0)
        self.letters = []

    def follow_routing_diagram(self, puzzle):
        routing_diagram = puzzle.split('\n')
        index = None
        for i, value in enumerate(routing_diagram[0]):
            if value is not ' ':
                index = i
                break
        max_width = max(len(a) for a in routing_diagram)
        routing_diagram = [str(a).ljust(max_width) for a in routing_diagram]
        self.cur_pos = (index, 0)

        move = self.get_next_move(routing_diagram)
        while move is not None:
            print(self.cur_pos, move)
            self.move(move)
            move = self.get_next_move(routing_diagram)

    def move(self, move):
        self.moves.append(move)
        self.cur_pos = (self.cur_pos[0] + move[0], self.cur_pos[1] + move[1])

    def get_next_move(self, routing_diagram):
        if len(self.moves) == 0:
            return 0, 1

        instruction = routing_diagram[self.cur_pos[1]][self.cur_pos[0]]
        if instruction == '+':
            if self.moves[-1][0] == 0:
                if self.cur_pos[0] + 1 < len(routing_diagram[self.cur_pos[1]]) and routing_diagram[self.cur_pos[1]][self.cur_pos[0] + 1] != ' ':
                    return 1, 0
                elif self.cur_pos[0] - 1 >= 0 and routing_diagram[self.cur_pos[1]][self.cur_pos[0] - 1] != ' ':
                    return -1, 0
            else:
                if self.cur_pos[1] + 1 < len(routing_diagram) and routing_diagram[self.cur_pos[1] + 1][self.cur_pos[0]] != ' ':
                    return 0, 1
                elif self.cur_pos[1] - 1 >= 0 and routing_diagram[self.cur_pos[1] - 1][self.cur_pos[0]] != ' ':
                    return 0, -1

        if instruction != ' ' and instruction != '|' and instruction != '-':
            self.letters.append(instruction)
            return self.moves[-1]

        if instruction == '|' or instruction == '-':
            return self.moves[-1]

        return None
