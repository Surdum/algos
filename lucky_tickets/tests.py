from checkers.tester import AlgoTester
from algorithms import SimpleEnumeration, SumOfSquares, FastLuckyNumbersCounter


if __name__ == '__main__':
    checker = AlgoTester(SimpleEnumeration)  # slow
    checker.check(3, 'tests')
    my = AlgoTester(SumOfSquares)  # little faster
    my.check(6, 'tests')
    # my.show_time_graph()
    my = AlgoTester(FastLuckyNumbersCounter)  # really fast
    my.check(10, 'tests')

    my.run_one_test(10, 3081918923741896840)
    my.run_one_test(20, 218768894829904122626725603838896148680)

