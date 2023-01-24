from checkers.tester import AlgoTester
from power import Iterative, Multiplication, BinaryExpansionOfTheExponent


if __name__ == '__main__':
    # checker = AlgoTester(Iterative)
    # checker.check(5, 'tests')
    # checker = AlgoTester(Multiplication)
    # checker.check(5, 'tests')
    checker = AlgoTester(BinaryExpansionOfTheExponent)
    checker.check(5, 'tests')


