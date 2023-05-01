from utils import get_left, get_right


class Auto:
    alphabet = 'ABC'
    pattern = ''
    delta = []

    def create_delta(self, pattern: str):
        self.pattern = pattern
        self.delta = [[0] * len(self.alphabet)] * len(pattern)
        for q in range(0, len(pattern)):
            for c in self.alphabet:
                line = get_left(pattern, q) + c
                k = q + 1
                while get_left(pattern, k) != get_right(line, k):
                    k -= 1
                self.delta[q][ord(c) - ord(self.alphabet[0])] = k

    def search(self, text: str) -> int:
        q = 0
        for i in range(0, len(text)):
            q = self.delta[q][ord(text[i]) - ord(self.alphabet[0])]
            if q == len(self.pattern):
                return i + 1
        return -1


if __name__ == '__main__':
    auto = Auto()
    auto.create_delta('AABAABAAABA')
    print(auto.search('ABA'))
    print(auto.search('BAA'))
