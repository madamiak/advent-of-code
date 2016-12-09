import re


class Puzzle0701:
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
        return not cls.has_abba(in_brackets) and cls.has_abba(outside_brackets)

    @classmethod
    def has_abba(cls, sequences):
        for sequence in sequences:
            for i in range(0, len(sequence) - 3):
                if sequence[i:i+2] != sequence[i+2:i+4] and sequence[i:i+4] == sequence[i:i+4:][::-1]:
                    return True
        return False
