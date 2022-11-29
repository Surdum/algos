from base import AlgoBase


class Iterative(AlgoBase):
    description = "Iterative power"

    def prepare_args(self, n, p):
        return float(n), float(p)

    def run(self, n, p):
        if p == 0:
            return 1.0
        t = n
        for i in range(int(p)-1):
            t *= n
        return round(t, 10)


class Multiplication(AlgoBase):
    description = "Multiplication"

    def prepare_args(self, n, p):
        return float(n), int(p)

    def run(self, n, p):
        res = 1.0
        while p > 0:
            i = 1
            t = n
            while i*2 < p:
                i *= 2
                t *= t
            res *= t
            p -= i
        return round(res, 10)


class BinaryExpansionOfTheExponent(AlgoBase):
    description = "Binary Expansion Of The Exponent"

    def prepare_args(self, n, p):
        return float(n), int(p)

    def run(self, n, p):
        d = n
        res = 1.
        for bit in bin(p)[2:][::-1]:
            if bit == '1':
                res *= d
            d *= d
        return round(res, 10)


if __name__ == '__main__':
    # sec = Multiplication()
    # print(sec.run(2, 64))
    # alg = Iterative()
    # print(alg.run(55, 10))
    b = BinaryExpansionOfTheExponent()
    print(b.run(2., 10))




