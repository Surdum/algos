from checkers import AlgoTester, PerformanceComparator
from algorithms import IterativeFibonacci, RecursiveFibonacci, \
    GolderRatioFibonacci, MatrixMultiplicationFibonacci
# import matplotlib.pyplot as plt


if __name__ == '__main__':
    performance = {}

    # algs = [IterativeFibonacci, RecursiveFibonacci, GolderRatioFibonacci, MatrixMultiplicationFibonacci]
    # iterations = 1000
    # tester_args = (7, '4.Fibo')
    #
    # perf_test = PerformanceComparator(algs)
    # perf_test.calculate(iterations, tester_args)
    # perf_test.show_graph('Fibonacci')

    algs = [IterativeFibonacci, GolderRatioFibonacci]
    iterations = 2000
    tester_args = (8, '4.Fibo')

    perf_test = PerformanceComparator(algs)
    perf_test.calculate(iterations, tester_args)
    perf_test.show_graph('Fibonacci')

    # checker = AlgoTester(IterativeFibonacci)
    # checker.check(7, '4.Fibo')
    # performance[checker.alg.description] = checker.performance
    # #
    # checker = AlgoTester(RecursiveFibonacci)
    # checker.check(7, '4.Fibo')
    # performance[checker.alg.description] = checker.performance
    # #
    # checker = AlgoTester(GolderRatioFibonacci)
    # checker.check(7, '4.Fibo')
    # performance[checker.alg.description] = checker.performance
    # #
    # checker = AlgoTester(MatrixMultiplicationFibonacci)
    # checker.check(7, '4.Fibo')
    # performance[checker.alg.description] = checker.performance



