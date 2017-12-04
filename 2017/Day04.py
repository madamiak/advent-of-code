import itertools


def same_words_count(word, words):
    return words.count(word)


def anagrams_count(word, words):
    return sum([words.count(''.join(combination)) for combination in set(itertools.permutations(word))])


class PassphraseValidator(object):
    def count_valid(self, puzzle, counting_function):
        passphrases = str.split(puzzle, '\n')
        result = 0
        for passphrase in passphrases:
            words = passphrase.split()
            if all([counting_function(word, words) == 1 for word in words]):
                result += 1
        return result
