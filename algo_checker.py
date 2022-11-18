from time import time
import os


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class AlgoChecker:
    name = "AlgoChecker by Babaev George"
    version = "13.11.2022"
    alg_class = None
    time_results = []

    def __init__(self, alg_class):
        self.alg = alg_class()
        self.print(f'======================================', Colors.UNDERLINE)
        print(f"{self.name}\nVersion: {self.version}\nAlgorithm: ", end='')
        self.print(f"{self.alg.description}", Colors.BOLD)

    def normalize_time(self, t):
        if int(t) > 0:
            return f"{int(t)}s"
        units = [(1000, 'ms'), (10**6, 'µs'), (10**9, 'ns')]
        i = 0
        while int((t - int(t)) * units[i][0]) <= 0 and i < len(units):
            i += 1
        return f"{int((t - int(t)) * units[i][0])}{units[i][1]}"

    def unify(self, s):
        return str(s).strip()

    def print(self, text, color, **kwargs):
        print(f"{color}{text}{Colors.ENDC}", **kwargs)

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
                       f'Total time: {self.normalize_time(total_time)}\n'
                       f'Test finished successfully.', Colors.OKGREEN)
        else:
            self.print(f'Input: {input_}\nExpected output: "{expected_output}"; Actual output: "{actual_out}"',
                       Colors.WARNING)
            self.print(f'Total time: {self.normalize_time(total_time)}\nTest finished unsuccessfully',
                       Colors.FAIL)
            return False
        return True

    def check(self, test_count, folder_with_tests):
        for i in range(test_count):
            self.print(f'======================================', Colors.HEADER)
            self.print(f'Test {i+1} started...', Colors.BOLD + Colors.OKCYAN)
            in_file = os.path.join(folder_with_tests, f'test.{i}.in')
            out_file = os.path.join(folder_with_tests, f'test.{i}.out')
            if not os.path.exists(in_file) or not os.path.exists(out_file):
                print(f'Test {i+1} ignored: no input or output file')
                continue

            inp = open(in_file).readline()
            inp = "" if not self.unify(inp) else self.unify(inp)

            expected_out = open(out_file).readline()
            expected_out = "" if not self.unify(expected_out) else self.unify(expected_out)

            start_time = time()
            try:
                args = inp.split() if inp else [inp]
                actual_out = self.alg.run(*self.alg.prepare_args(*args))
            except Exception as e:
                actual_out = f'ERROR: {e}'
            total_time = time() - start_time
            self.time_results.append(total_time)
            if not self.unify(actual_out).startswith('ERROR') and self.unify(expected_out) == self.unify(actual_out):
                self.print(f'Input: {inp}\n'
                           f'Output: {actual_out}\n'
                           f'Total time: {self.normalize_time(total_time)}\n'
                           f'Test {i+1} finished successfully.', Colors.OKGREEN)
            else:
                self.print(f'Input: {inp}\nExpected output: "{expected_out}"; Actual output: "{actual_out}"', Colors.WARNING)
                self.print(f"Input file: {in_file}; Output file: {out_file}", Colors.WARNING)
                self.print(f'Total time: {self.normalize_time(total_time)}\nTest {i+1} finished unsuccessfully', Colors.FAIL)
                return False
        return True

    def show_time_graph(self):
        try:
            import matplotlib.pyplot as plt

            plt.plot(self.time_results)
            # plt.ylabel('some numbers')
            plt.show()

        except ImportError:
            self.print('Please, install matplotlib first!', Colors.WARNING)