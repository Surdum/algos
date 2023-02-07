from testers import AlgoTester, PerformanceComparatorWithGraph
from algorithms import IterativeFibonacci, RecursiveFibonacci, \
    GolderRatioFibonacci, MatrixMultiplicationFibonacci
# import matplotlib.pyplot as plt


if __name__ == '__main__':

    # algs = [IterativeFibonacci, RecursiveFibonacci, GolderRatioFibonacci, MatrixMultiplicationFibonacci]
    # iterations = 2000
    # tester_args = (7, 'tests')
    #
    # perf_test = PerformanceComparatorWithGraph(algs)
    # perf_test.calculate(iterations, tester_args)
    # perf_test.show_graph('Fibonacci')

    checker = AlgoTester(IterativeFibonacci)
    checker.check(8, 'tests', skip_tests=7)
    #
    checker = AlgoTester(RecursiveFibonacci)
    checker.check(7, 'tests', skip_tests=6)
    #
    checker = AlgoTester(GolderRatioFibonacci)
    checker.check(7, 'tests', skip_tests=6)
    #
    checker = AlgoTester(MatrixMultiplicationFibonacci)
    checker.check(10, 'tests', skip_tests=9)



