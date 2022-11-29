from .utils import ColorPrint, Colors, normalize_time
from time import time
import os


class AlgoTester(ColorPrint):
    name = "AlgoTester by Babaev George"
    version = "26.11.2022"
    alg_class = None
    performance = []
    no_out = False
    # time_results = []

    def __init__(self, alg_class, no_out=False):
        self.no_out = no_out
        self.alg = alg_class()
        self.print(f'======================================', Colors.UNDERLINE)
        self.print(f"{self.name}\nVersion: {self.version}\nAlgorithm: ", end='')
        self.print(f"{self.alg.description}", Colors.BOLD)

    def unify(self, s):
        return str(s).strip()

    def print(self, text, color='', **kwargs):
        if not self.no_out:
            self.__init__(ColorPrint).print(text, color, **kwargs)

    def run_one_test(self, input_, expected_output):
        self.print(f'======================================', Colors.HEADER)
        self.print(f'Test started...', Colors.BOLD + Colors.OKCYAN)
        start_time = time()
        try:
            actual_out = self.alg.run(input_)
        except Exception as e:
            actual_out = f'ERROR: {e}'
        total_time = time() - start_time

        if not str(actual_out).startswith('ERROR') and actual_out == expected_output:
            self.print(f'Input: {input_}\n'
                       f'Output: {actual_out}\n'
                       f'Total time: {normalize_time(total_time)}\n'
                       f'Test finished successfully.', Colors.OKGREEN)
        else:
            self.print(f'Input: {input_}\nExpected output: "{expected_output}"; Actual output: "{actual_out}"',
                       Colors.WARNING)
            self.print(f'Total time: {normalize_time(total_time)}\nTest finished unsuccessfully',
                       Colors.FAIL)
            return False
        return True

    def check(self, test_count, folder_with_tests, no_out=None):
        if no_out is not None:
            self.no_out = no_out
        self.performance = []
        for i in range(test_count):
            self.print(f'======================================', Colors.HEADER)
            self.print(f'Test {i+1} started...', Colors.BOLD + Colors.OKCYAN)
            in_file = os.path.join(folder_with_tests, f'test.{i}.in')
            out_file = os.path.join(folder_with_tests, f'test.{i}.out')
            if not os.path.exists(in_file) or not os.path.exists(out_file):
                self.print(f'Test {i+1} ignored: no input or output file')
                continue

            inp = open(in_file).read()
            inp = "" if not self.unify(inp) else self.unify(inp)

            expected_out = open(out_file).read()
            expected_out = "" if not self.unify(expected_out) else self.unify(expected_out)

            start_time = time()
            try:
                args = inp.split('\n') if inp else [inp]
                actual_out = self.alg.run(*self.alg.prepare_args(*args))
            except Exception as e:
                actual_out = f'ERROR: {e}'
            total_time = time() - start_time
            self.performance.append((inp, total_time))
            if not self.unify(actual_out).startswith('ERROR') and self.unify(expected_out) == self.unify(actual_out):
                self.print(f'Input: {inp}\n'
                           f'Output: {actual_out if len(str(actual_out)) < 50 else (str(actual_out)[:50] + f"... + {len(str(actual_out)) - 50} signs")}\n'
                           f'Total time: {normalize_time(total_time)}\n'
                           f'Test {i+1} finished successfully.', Colors.OKGREEN)
            else:
                self.print(f'Input: {inp}\nExpected output: "{expected_out}"; Actual output: "{actual_out}"', Colors.WARNING)
                self.print(f"Input file: {in_file}; Output file: {out_file}", Colors.WARNING)
                self.print(f'Total time: {normalize_time(total_time)}\nTest {i+1} finished unsuccessfully', Colors.FAIL)
                return False
        return True

    def show_time_graph(self):
        try:
            import matplotlib.pyplot as plt

            plt.plot([elem[1] for elem in self.performance])
            # plt.ylabel('some numbers')
            plt.show()

        except ImportError:
            self.print('Please, install matplotlib first!', Colors.WARNING)
