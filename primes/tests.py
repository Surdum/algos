from checkers import AlgoTester
from primes.algorithms import PrimeNumbersCount, SieveOfEratosthenes


if __name__ == '__main__':
    # checker = AlgoTester(PrimeNumbersCount)
    # checker.check(10, 'tests')

    checker = AlgoTester(SieveOfEratosthenes)
    checker.check(12, 'tests')
