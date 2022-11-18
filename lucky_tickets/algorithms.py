from base import AlgoBase
from collections import defaultdict


class SimpleEnumeration(AlgoBase):
    description = 'Simple enumeration of all numbers in two loops'

    def prepare_args(self, n: str) -> list:
        return [int(n)]

    def run(self, n):
        s = 0  # sum
        for i in range(int(n * '9') + 1):
            for j in range(int(n * '9') + 1):
                if sum([int(elem) for elem in str(i)]) == sum([int(elem) for elem in str(j)]):
                    s += 1
        return s


class SumOfSquares(AlgoBase):
    description = 'Calculate sums of the digits of any number, square it and sum in result'

    def prepare_args(self, n: str) -> list:
        return [int(n)]

    def run(self, n):
        sums = defaultdict(int)
        for i in range((int(n * '9') + 1)):
            s = sum([int(elem) for elem in str(i)])
            sums[s] += 1
        return sum([v**2 for v in sums.values()])


class FastLuckyNumbersCounter(AlgoBase):
    description = 'Fastest algorithm of calculating lucky number count for 2N ticket'

    def prepare_args(self, n: str) -> list:
        return [int(n)]

    def run(self, n):
        t = [1]
        for j in range(1, n + 1):
            p = [0 for _ in range(j * 9 + 1)]
            for i in range(len(t)):
                for k in range(i, i + 10):
                    p[k] += t[i]
            t = p
        return sum([elem ** 2 for elem in t])


if __name__ == '__main__':
    fast_counter = FastLuckyNumbersCounter()
    print(fast_counter.run(30))


