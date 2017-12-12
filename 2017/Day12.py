class DigitalPlumber(object):
    def count_programs(self, puzzle):
        pipes = [Pipe(row) for row in str.split(puzzle, '\n')]
        groups = {}
        while len(pipes) > 0:
            visited = [pipes[0].connection]
            self._visit_pipes(pipes[0], pipes, visited)
            groups[visited[0]] = len(visited)
        return groups

    def _visit_pipes(self, pipe, pipes, visited):
        for connection in pipe.connections:
            if connection not in visited:
                visited.append(connection)
                for connected_pipe in pipes:
                    if connected_pipe.connection == connection:
                        self._visit_pipes(connected_pipe, pipes, visited)
                        break
        if pipe in pipes:
            pipes.remove(pipe)


class Pipe(object):
    def __init__(self, row) -> None:
        parts = str.split(row, '<->')
        self.connection = int(parts[0].strip())
        self.connections = [int(s.strip()) for s in str.split(parts[1], ',')]

    def __repr__(self):
        return str(self.connection)

    def __eq__(self, other):
        return self.connection == other.connection
