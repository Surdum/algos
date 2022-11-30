from checkers import AlgoTester
from primes.algorithms import PrimeNumbersCount, SieveOfEratosthenes


if __name__ == '__main__':
    # checker = AlgoTester(PrimeNumbersCount)
    # checker.check(10, '5.Primes')

    checker = AlgoTester(SieveOfEratosthenes)
    checker.check(12, '5.Primes')
