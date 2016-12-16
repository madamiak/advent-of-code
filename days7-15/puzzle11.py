from itertools import combinations

import copy

import sys


class Puzzle11:
    def __init__(self):
        pass

    directions = {'UP': 1, 'DOWN': -1}
    solutions = set()

    @classmethod
    def solve(cls, state, initial=0, visited=[]):
        print 'Step ' + str(initial) + ':'
        # if initial == 0:
        #     if state == [['LM'], ['E', 'HM', 'HG'], ['LG'], []]:
        #         pass
        visited.append(state)
        cls.print_state(state)

        if cls.solved(state):
            return initial

        valid_moves = []
        for direction in cls.get_possible_directions(state):
            for combination in cls.get_possible_combinations(state):
                if cls.valid_move(direction, combination, state, visited):
                    valid_moves.append([direction, combination])

        if len(valid_moves) == 0:
            return sys.maxint

        for move in sorted(valid_moves, key=lambda v: v[0])[::-1]:
            new_state = cls.move(move[1], move[0], copy.deepcopy(state))
            if initial == 0:
                pass
            print 'Moving ' + str(move[0]) + ' with items ' + str(move[1])
            cls.solutions.add(cls.solve(new_state, initial + 1, copy.copy(visited)))

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
        return cls.valid_left_floor(combination, state) and cls.not_visited(direction, combination, state, visited)

    @classmethod
    def valid_left_floor(cls, combination, state):
        cur_floor = cls.get_cur_floor(state)
        left_items = filter(lambda x: x not in combination, state[cur_floor])
        for item in left_items:
            item_compatibility = item[:1]
            item_type = item[1:]
            if item_type == 'M' and any(x[1:] == 'G' for x in left_items) and item_compatibility + 'G' not in left_items:
                return False
        return True

    @classmethod
    def not_visited(cls, direction, combination, state, visited):
        return cls.move(combination, direction, copy.deepcopy(state)) not in visited

    @classmethod
    def solved(cls, state):
        return all(x == [] for x in state[:-1])
