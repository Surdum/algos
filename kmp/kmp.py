from utils import get_left, get_right


class KMP:
    pi = []

    def create_pi_slow(self, pattern: str) -> None:
        self.pi = [0] * (len(pattern) + 1)
        for q in range(len(pattern) + 1):
            line = get_left(pattern, q)
            for d in range(q):
                if get_left(line, d) == get_right(line, d):
                    self.pi[q] = d

    def create_pi_fast(self, pattern: str) -> None:
        self.pi = [0] * (len(pattern) + 1)
        self.pi[1] = 0
        for q in range(1, len(pattern)):
            d = self.pi[q]
            while d > 0 and pattern[d] != pattern[q]:
                d = self.pi[d]
            if pattern[d] == pattern[q]:
                d += 1
            self.pi[q + 1] = d


if __name__ == '__main__':
    auto = KMP()
    auto.create_pi_slow('AABAABAAABA')
    print(auto.pi)

