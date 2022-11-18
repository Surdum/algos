from algo_checker import *
from classes import SimpleEnumeration, SumOfSquares, FastLuckyNumbersCounter


if __name__ == '__main__':
    # checker = AlgoChecker(SimpleEnumeration)  # slow
    # checker.check(3, '1.Tickets')
    # my = AlgoChecker(SumOfSquares)  # little faster
    # my.check(7, '1.Tickets')
    # my.show_time_graph()
    my = AlgoChecker(FastLuckyNumbersCounter)  # really fast
    my.check(10, '1.Tickets')

    my.run_one_test(10, 3081918923741896840)
    my.run_one_test(20, 218768894829904122626725603838896148680)

