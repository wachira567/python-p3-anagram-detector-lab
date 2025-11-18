class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        sorted_word = sorted(self.word)
        return [w for w in words if sorted(w) == sorted_word]
