from .tester import AlgoTester
from .utils import Colors, ColorPrint, normalize_time
from time import time
from copy import deepcopy


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


class SortPerformanceComparator(ColorPrint):
    results: list = []
    input_data_len: list = []

    def calculate(self, algorithms, dataset, additional_vars=None, iterations=1, print_steps=False):
        if additional_vars is None:
            additional_vars = []
        if not self.input_data_len:
            self.input_data_len.extend([len(data[0]) for data in dataset])
        for algo in algorithms:
            if print_steps:
                print(algo().description)
            t = {'name': algo().description, 'performance': [],
                 'additional_vars': {av: [] for av in additional_vars}}
            for data in dataset:
                p = 0
                for i in range(iterations):
                    if print_steps:
                        print(f'run {len(data[0])} {i+1}/{iterations}')
                    start = time()
                    runner = algo()
                    runner.run(*deepcopy(data))
                    p += time() - start
                    if i == 0 and additional_vars:
                        for av in additional_vars:
                            t['additional_vars'][av].append(runner.vars[av])
                t['performance'].append(p / iterations)
            ind = None
            for i, r in enumerate(self.results):
                if r['name'] == algo.description:
                    ind = i
                    break
            if ind is not None:
                for i in range(len(self.results[ind]['performance'])):
                    self.results[ind]['performance'][i] = (self.results[ind]['performance'][i] + t['performance'][i]) / 2
            else:
                self.results.append(t)

    def print_results(self):
        max_len = 1
        for i, result in enumerate(self.results):
            for item in [normalize_time(p) for p in result['performance']] + \
                        [str(i) for i in self.input_data_len] + \
                        sum(result['additional_vars'].values(), []):
                max_len = max(max_len, len(str(item)))
        n = max_len + 1
        for result in self.results:
            print(result['name'].rjust(n * (len(self.results[0]['performance']) + 1)))
            print('N'.rjust(n, " "), end="")
            for inp_len in self.input_data_len:
                print(str(inp_len).rjust(n, " "), end="")
            print()
            print('time'.rjust(n, " "), end="")
            for p in result['performance']:
                print(normalize_time(p).rjust(n, " "), end="")
            print()
            for k, v in result['additional_vars'].items():
                print(k.rjust(n, " "), end="")
                for item in v:
                    print(str(item).rjust(n, " "), end="")
                print()
            print()

    def print_csv(self):
        p = [[] for _ in range(len(self.results[0]['performance']) + 1)]
        for ind, res in enumerate(self.results):
            p[0].append(res['name'])
            for i, time_ in enumerate(res['performance']):
                p[i+1].append(str(normalize_time(time_)))
        s = []
        for row in p:
            s.append(';'.join(row))
        print('\n'.join(s))
