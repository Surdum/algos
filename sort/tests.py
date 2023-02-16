from sort import *
from testers.performance import SortPerformanceComparator
from utils import generate_shuffled_number_sequence, generate_random_number_sequence
import sys


sys.setrecursionlimit(1_000_000)

tester = SortPerformanceComparator()

seq_10_2 = generate_shuffled_number_sequence(10**2)
seq_10_3 = generate_shuffled_number_sequence(10**3)
seq_10_4 = generate_shuffled_number_sequence(10**4)
seq_10_5 = generate_shuffled_number_sequence(10**5)
seq_10_6 = generate_shuffled_number_sequence(10**6)

rnd_10_2 = generate_random_number_sequence(10**2, 999)
rnd_10_3 = generate_random_number_sequence(10**3, 999)
rnd_10_4 = generate_random_number_sequence(10**4, 999)
rnd_10_5 = generate_random_number_sequence(10**5, 999)
rnd_10_6 = generate_random_number_sequence(10**6, 999)

# slow
# tester.calculate(algorithms=[BubbleSort, BubbleSortOptimized, InsertionSort, InsertionSortOptimized,
#                              InsertionSortShift, InsertionSortBinary,
#                              SelectionSort, HeapSort, ],
#                  dataset=[[seq_10_2], [seq_10_3], [seq_10_4], ],  # [seq_10_5], ],  # [seq_10_6]],
#                  additional_vars=["cmp", "asg"],
#                  iterations=5)
# tester.print_results()

# fast
# tester.calculate(algorithms=[ShellSort, ShellSort4, ShellSort8, HeapSortRecursive, QuickSort, MergeSort],
#                  dataset=[[seq_10_2], [seq_10_3], [seq_10_4], [seq_10_5], ],  # [seq_10_6]],
#                  additional_vars=["cmp", "asg"],
#                  iterations=20)
# tester.print_results()

# very fast
tester.calculate(algorithms=[BucketSort, CountingSort, RadixSort],
                 dataset=[[rnd_10_2], [rnd_10_3], [rnd_10_4], [rnd_10_5], [rnd_10_6]],
                 additional_vars=["cmp", "asg"],
                 iterations=20)
tester.print_results()

