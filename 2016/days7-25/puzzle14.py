import hashlib


class Puzzle14:
    def __init__(self):
        self.candidate_key = None
        self.keys = []
        self.cache = {}
        pass

    def solve(self, puzzle, part=1):
        index = 0
        while True:
            if index == 7858:
                pass
            if len(self.keys) == 64:
                return
            candidate_key = puzzle + str(index)
            md5 = self.generate_md5(candidate_key, part)
            cur_c = md5[0]
            cur_o = 1
            for c in md5[1:]:
                if c == cur_c:
                    cur_o += 1
                    if cur_o == 3:
                        self.candidate_key = index
                        if self.has_five_of_a_kind(cur_c, puzzle, index + 1, part):
                            self.keys.append(index)
                        break
                else:
                    cur_c = c
                    cur_o = 1
            index += 1
        pass

    def generate_md5(self, input, part):
        if part == 1:
            if input in self.cache:
                return self.cache[input]
            m = hashlib.md5()
            m.update(input)
            hash = m.hexdigest()
            self.cache[input] = hash
            return hash
        if part == 2:
            hash = self.generate_md5(input, 1)
            for i in range(2016):
                hash = self.generate_md5(hash, 1)
            return hash

    def get_first_candidate_index(self):
        return self.candidate_key

    def has_five_of_a_kind(self, char, puzzle, index, part):
        for i in range(index, index + 1000):
            key = puzzle + str(i)
            md5 = self.generate_md5(key, part)
            cur_o = 0
            for c in md5[1:]:
                if cur_o == 5:
                    # print 'in 1000', key, md5, char
                    return True
                if c == char:
                    cur_o += 1
                else:
                    cur_o = 0
        return False

    def get_key_at_index(self, index):
        print self.keys
        return self.keys[index]
