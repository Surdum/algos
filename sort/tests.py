from sort import *
from testers.performance import SortPerformanceComparator
from utils import generate_random_number_sequence


tester = SortPerformanceComparator()

seq_10_2 = generate_random_number_sequence(10**2)
seq_10_3 = generate_random_number_sequence(10**3)
seq_10_4 = generate_random_number_sequence(10**4)
seq_10_5 = generate_random_number_sequence(10**5)
seq_10_6 = generate_random_number_sequence(10**6)

# tester.calculate(algorithms=[BubbleSort, BubbleSortOptimized, InsertionSort, InsertionSortOptimized,
#                              InsertionSortShift, InsertionSortBinary, ShellSort, ShellSort4, ShellSort8],
#                  dataset=[[seq_10_2], [seq_10_3], [seq_10_4], [seq_10_5], [seq_10_6]],
#                  additional_vars=["cmp", "asg"],
#                  iterations=3)
# tester.print_results()

tester.calculate(algorithms=[SelectionSort, HeapSort],
                 dataset=[[seq_10_2], [seq_10_3], [seq_10_4]],
                 additional_vars=["cmp", "asg"],
                 iterations=3)
tester.print_results()
