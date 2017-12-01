from itertools import combinations

import copy

import sys


class Puzzle11:
    def __init__(self):
        pass

    directions = {'UP': 1, 'DOWN': -1}
    solutions = set()

    @classmethod
    def solve(cls, state, steps=0, visited=[]):
        if steps == 0:
            cls.generate_alphabet(state)
        if steps > 9:
            return sys.maxint

        if cls.solved(state):
            return steps

        # print 'Step ' + str(initial) + ':'
        cls.visit(copy.deepcopy(state), visited)
        # cls.print_state(state)

        valid_moves = []
        for direction in cls.get_possible_directions(state):
            for combination in cls.get_possible_combinations(state):
                if cls.valid_move(direction, combination, state, visited):
                    valid_moves.append([direction, combination])

        if len(valid_moves) == 0:
            return sys.maxint

        up_moves = filter(lambda x: x[0] == 1, valid_moves)
        down_moves = filter(lambda x: x[0] == -1, valid_moves)
        preferred_up_moves = filter(lambda x: len(x[1]) == 3, up_moves)
        preferred_down_moves = filter(lambda x: len(x[1]) == 2, down_moves)
        filtered_moves = (preferred_up_moves if len(preferred_up_moves) > 0 else up_moves) + \
                         (preferred_down_moves if len(preferred_down_moves) > 0 else down_moves)

        for move in filtered_moves:
            new_state = cls.move(move[1], move[0], copy.deepcopy(state))
            # print 'Moving ' + str(move[0]) + ' with items ' + str(move[1])
            r = cls.solve(new_state, steps + 1, visited)
            cls.solutions.add(r)
        return min(cls.solutions)

    @classmethod
    def generate_alphabet(cls, state):
        cls.alphabet = filter(lambda x: x != 'E', set([x[:1] for sublist in state for x in sublist]))
        cls.perms = list(combinations(cls.alphabet, 2))

    @classmethod
    def visit(cls, state, visited):
        [visited.append(s) for s in cls.generate_interchangeable_states(state)]

    @classmethod
    def generate_interchangeable_states(cls, state):
        states = [copy.deepcopy(state)]
        for perm in cls.perms:
            new_state = [[] for i in range(len(state))]
            for i in range(len(state)):
                for item in state[i]:
                    if perm[0] in item:
                        new_state[i].append(str(item).replace(perm[0], perm[1]))
                    elif perm[1] in item:
                        new_state[i].append(str(item).replace(perm[1], perm[0]))
                    else:
                        new_state[i].append(item)
            states.append(new_state)
        return states

    @classmethod
    def get_possible_directions(cls, state):
        return filter(lambda i: cls.get_cur_floor(state) + i in range(len(state)), cls.directions.itervalues())

    @classmethod
    def get_possible_combinations(cls, state):
        cur_items = state[cls.get_cur_floor(state)]
        return filter(lambda i: 'E' in i,
                      list(combinations(cur_items, 2)) + list(combinations(cur_items, 3)))

    @classmethod
    def get_cur_floor(cls, state):
        return [x for x, y in enumerate(state) if 'E' in state[x]][0]

    @classmethod
    def move(cls, items, direction, state):
        cur_floor = cls.get_cur_floor(state)
        [state[cur_floor].remove(item) for item in items]
        [state[cur_floor + direction].insert(0, item) for item in items[::-1]]
        return state

    @classmethod
    def print_state(cls, state):
        floors = state[::-1]
        for i in range(len(floors)):
            print floors[i]

    @classmethod
    def valid_move(cls, direction, combination, state, visited):
        return cls.valid_left_floor(combination, state) and cls.valid_next_floor(direction, combination, state) \
               and cls.not_visited(direction, combination, state, visited)

    @classmethod
    def valid_left_floor(cls, combination, state):
        cur_floor = cls.get_cur_floor(state)
        left_items = filter(lambda x: x not in combination, state[cur_floor])
        for item in left_items:
            item_compatibility = item[:1]
            item_type = item[1:]
            if item_type == 'M' and any(
                            x[1:] == 'G' for x in left_items) and item_compatibility + 'G' not in left_items:
                return False
        return True

    @classmethod
    def valid_next_floor(cls, direction, combination, state):
        cur_floor = cls.get_cur_floor(state)
        new_items = list(combination) + state[cur_floor + direction]
        for item in new_items:
            item_compatibility = item[:1]
            item_type = item[1:]
            if item_type == 'M' and any(
                            x[1:] == 'G' for x in new_items) and item_compatibility + 'G' not in new_items:
                return False
        return True

    @classmethod
    def not_visited(cls, direction, combination, state, visited):
        return cls.move(combination, direction, copy.deepcopy(state)) not in visited

    @classmethod
    def solved(cls, state):
        return all(x == [] for x in state[:-1])
