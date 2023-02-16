from sort import *
from testers.performance import SortPerformanceComparator
from utils import generate_shuffled_number_sequence
import sys


sys.setrecursionlimit(1_000_000)

tester = SortPerformanceComparator()

seq_10_2 = generate_shuffled_number_sequence(10**2)
seq_10_3 = generate_shuffled_number_sequence(10**3)
seq_10_4 = generate_shuffled_number_sequence(10**4)
seq_10_5 = generate_shuffled_number_sequence(10**5)
seq_10_6 = generate_shuffled_number_sequence(10**6)

tester.calculate(algorithms=[BubbleSort, BubbleSortOptimized, InsertionSort, InsertionSortOptimized,
                             InsertionSortShift, InsertionSortBinary, ShellSort, ShellSort4, ShellSort8,
                             SelectionSort, HeapSort, ],  # HeapSortRecursive],
                 dataset=[[seq_10_2], ],  # [seq_10_3], [seq_10_4], ],  # [seq_10_5], ],  # [seq_10_6]],
                 additional_vars=["cmp", "asg"],
                 iterations=1)
tester.print_results()
