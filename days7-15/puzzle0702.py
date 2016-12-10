import re


class Puzzle0702:
    def __init__(self):
        pass

    @classmethod
    def solve(cls, puzzle):
        return len(filter(lambda x: x, map(lambda ip: cls.is_tls_supported(ip), re.split("\n", puzzle))))

    @classmethod
    def is_tls_supported(cls, ip):
        bracket_content = r"\[([A-Za-z0-9_]+)\]"
        in_brackets = re.findall(bracket_content, ip)
        outside_brackets = re.sub(bracket_content, "|", ip).split('|')
        for outside_bracket in outside_brackets:
            for i in range(len(outside_bracket) - 2):
                if outside_bracket[i] == outside_bracket[i + 2] and outside_bracket[i] != outside_bracket[i + 1]:
                    for in_bracket in in_brackets:
                        for j in range(len(in_bracket) - 2):
                            if in_bracket[j] == in_bracket[j + 2] == outside_bracket[i + 1] \
                                    and in_bracket[j + 1] == outside_bracket[i]:
                                return True
        return False
