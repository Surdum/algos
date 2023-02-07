from .tester import AlgoTester
from .utils import Colors, ColorPrint


class PerformanceComparatorWithGraph(ColorPrint):
    performance = {}
    iterations = 0

    def __init__(self, alg_classes):
        self.alg_classes = alg_classes

    def calculate(self, iterations, tester_args):
        self.iterations = iterations
        for alg in self.alg_classes:
            checker = AlgoTester(alg, no_out=True)
            results = []
            for _ in range(iterations):
                checker.check(*tester_args)
                results.append(checker.performance)
            average_result = []
            for i in range(len(results[0])):
                t = 0
                for j in range(iterations):
                    t += results[j][i][1]
                t /= float(iterations)
                average_result.append((results[0][i][0], t))
            self.performance[checker.alg.description] = average_result

    def show_graph(self, title, remove_title_from_legend=True):
        try:
            import matplotlib.pyplot as plt

            for desc, perf in self.performance.items():
                if remove_title_from_legend:
                    desc = desc.lower().replace(title.lower(), '')
                plt.plot([elem[1] for elem in perf], label=desc)
            plt.title(f'{title} - average by {self.iterations} iterations')
            plt.legend()
            plt.show()

        except ImportError:
            self.print('Please, install matplotlib first!', Colors.WARNING)
