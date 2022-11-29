from base import AlgoBase
from power.algorithms import Multiplication
from utils import MatrixOperations


class RecursiveFibonacci(AlgoBase):
    description = 'Recursive fibonacci'

    def prepare_args(self, n: str):
        return [int(n)]

    def fib(self, n):
        if n > 0:
            return self.fib(n - 1) + self.fib(n - 2)
        return 0 if n == 0 else 1

    def run(self, n):
        return self.fib(n)


class IterativeFibonacci(AlgoBase):
    description = 'Iterative fibonacci'

    def prepare_args(self, n: str):
        return [int(n)]

    def run(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a


class GolderRatioFibonacci(AlgoBase):
    description = 'Fibonacci golder ratio formula'

    def prepare_args(self, n: str):
        return [int(n)]

    def run(self, n):
        from math import sqrt
        fi = (1. + sqrt(5.)) * 0.5
        fi_n = Multiplication().run(fi, n)
        return int(fi_n / sqrt(5) + 0.5)


class MatrixMultiplicationFibonacci(AlgoBase):
    description = 'Fibonacci matrix multiplication'

    def prepare_args(self, n: str):
        return [int(n)]

    def run(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        matrix_op = MatrixOperations()
        base_matrix = \
            [[1, 1],
             [1, 0]]
        new_matrix = matrix_op.power(base_matrix, n-1)
        return new_matrix[0][0]


# 0 1 1 2 3 5 8 13 21 34
if __name__ == '__main__':
    rec = RecursiveFibonacci()
    print(rec.run(15))

    it = IterativeFibonacci()
    print(it.run(15))

    golden_ratio = GolderRatioFibonacci()
    print(golden_ratio.run(15))

    mat = MatrixMultiplicationFibonacci()
    print(mat.run(15))





