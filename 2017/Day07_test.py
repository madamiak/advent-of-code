from unittest import TestCase

from Day07 import TowerTree


class TestTowerTree(TestCase):
    def setUp(self):
        self.tower_tree = TowerTree()

    def test_1_1(self):
        self.assertEqual(self.tower_tree.balance_tree("pbga (66)\n"
                                                      "xhth (57)\n"
                                                      "ebii (61)\n"
                                                      "havc (66)\n"
                                                      "ktlj (57)\n"
                                                      "fwft (72) -> ktlj, cntj, xhth\n"
                                                      "qoyq (66)\n"
                                                      "padx (45) -> pbga, havc, qoyq\n"
                                                      "tknk (41) -> ugml, padx, fwft\n"
                                                      "jptl (61)\n"
                                                      "ugml (68) -> gyxo, ebii, jptl\n"
                                                      "gyxo (61)\n"
                                                      "cntj (57)").root.name, 'tknk')

    def test_puzzle_1(self):
        with open('Day07_puzzle.txt', 'r') as puzzle_file:
            tree = self.tower_tree.balance_tree(puzzle_file.read())
            print(tree.root.name)
            print(tree.unbalanced)

    def test_2_1(self):
        self.assertEqual(self.tower_tree.balance_tree("pbga (66)\n"
                                                      "xhth (57)\n"
                                                      "ebii (61)\n"
                                                      "havc (66)\n"
                                                      "ktlj (57)\n"
                                                      "fwft (72) -> ktlj, cntj, xhth\n"
                                                      "qoyq (66)\n"
                                                      "padx (45) -> pbga, havc, qoyq\n"
                                                      "tknk (41) -> ugml, padx, fwft\n"
                                                      "jptl (61)\n"
                                                      "ugml (68) -> gyxo, ebii, jptl\n"
                                                      "gyxo (61)\n"
                                                      "cntj (57)").unbalanced, 60)
