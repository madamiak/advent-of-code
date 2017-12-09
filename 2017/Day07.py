class TowerTree(object):
    def __init__(self) -> None:
        self.root = None
        self.unbalanced = None
        self.towers = []

    def balance_tree(self, puzzle):
        towers = [Node(row) for row in str.split(puzzle, '\n')]
        root_candidates = towers[::]
        for parent in list(filter(lambda x: len(x.children) > 0, towers)):
            for child in parent.children[::]:
                for tower in towers[::]:
                    if tower.name == child:
                        root_candidates.remove(tower)
        towers.remove(root_candidates[0])
        self.root = root_candidates[0]
        self._expand_node(self.root, towers)
        self.unbalanced = self.root.unbalanced()
        return self

    def _expand_node(self, parent, towers):
        for child in parent.children[::]:
            for tower in towers[::]:
                if child == tower.name:
                    towers.remove(tower)
                    parent.children.remove(child)
                    parent.children.append(tower)
                    break
        for child in parent.children:
            if len(child.children) > 0:
                self._expand_node(child, towers)


class Node(object):
    def __init__(self, row) -> None:
        parts = str.split(row, '->')[0].split()
        self.name = parts[0]
        self.weight = int(parts[1][1:-1])
        self.children = [node_name.strip() for node_name in str.split(str.split(row, '->')[1], ',')] if len(
            str.split(row, '->')) > 1 else []

    def __repr__(self) -> str:
        return "(name = " + self.name + \
               ", weight = " + str(self.weight) + \
               ", children = " + str(self.children) + \
               ")"

    def eval(self):
        return self.weight + sum([child.eval() for child in self.children])

    def balanced_children(self):
        weights = set()
        for child in self.children:
            weights.add(child.eval())
        return len(weights) == 1

    def unbalanced(self):
        b = [child.balanced_children() for child in self.children]
        if all(b):
            weights = []
            for child in self.children:
                weights.append(child.eval())
            weights = sorted(weights)
            if len(set(weights)) > 1:
                if weights[0] == weights[1]:
                    for child in self.children:
                        if child.eval() == weights[-1]:
                            return child.weight - child.eval() + weights[0]
                else:
                    for child in self.children:
                        if child.eval() == weights[0]:
                            return child.weight - child.eval() + weights[-1]
            else:
                return 0
        else:
            for child in self.children:
                result = child.unbalanced()
                if result > 0:
                    return result
