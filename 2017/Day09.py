class StreamEvaluator(object):
    def eval(self, puzzle):
        score, garbage, group_level = 0, 0, 0
        is_garbage, is_ignored = False, False
        for sign in puzzle:
            if not is_ignored:
                if sign == '!':
                    is_ignored = True
                elif sign == '<' and not is_garbage:
                    is_garbage = True
                elif sign == '>':
                    is_garbage = False
                elif not is_garbage:
                    if sign == '{':
                        group_level += 1
                        score += group_level
                    elif sign == '}':
                        group_level -= 1
                else:
                    garbage += 1
            else:
                is_ignored = False
        return score, garbage
