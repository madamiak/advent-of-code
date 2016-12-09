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
        return False
