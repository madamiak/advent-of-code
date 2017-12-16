import string


class PermutationPromenade(object):
    def dance(self, puzzle, programs, dances=1):
        moves = str.split(puzzle, ",")
        standings = list(string.ascii_lowercase)[:programs]
        visited = []
        for i in range(dances):
            s = "".join(standings)
            if s in visited:
                return visited[dances % i]
            visited.append(s)
            for move in moves:
                standings = self._parse_move(move, standings)
        return "".join(standings)

    def _parse_move(self, move, standings):
        if move[0] == "s":
            position = int(move[1:])
            standings = standings[-position:] + standings[:-position]
        elif move[0] == "x":
            position_1 = int(str.split(move[1:], "/")[0])
            position_2 = int(str.split(move[1:], "/")[1])
            standings[position_1], standings[position_2] = standings[position_2], standings[position_1]
        elif move[0] == "p":
            program_1 = str.split(move[1:], "/")[0]
            program_2 = str.split(move[1:], "/")[1]
            position_1 = standings.index(program_1)
            position_2 = standings.index(program_2)
            standings[position_1], standings[position_2] = standings[position_2], standings[position_1]
        return standings
