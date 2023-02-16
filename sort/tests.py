from sort import *
from testers.performance import SortPerformanceComparator
from utils import generate_shuffled_number_sequence as shf, generate_random_number_sequence as rnd
import sys


sys.setrecursionlimit(1_000_000)



seq_10_2 = shf(10**2)
seq_10_3 = shf(10**3)
seq_10_4 = shf(10**4)
seq_10_5 = shf(10**5)
seq_10_6 = shf(10**6)

# slow
# tester = SortPerformanceComparator()
# tester.calculate(algorithms=[BubbleSort, BubbleSortOptimized, InsertionSort, InsertionSortOptimized,
#                              InsertionSortShift, InsertionSortBinary,
#                              SelectionSort, HeapSort, ],
#                  dataset=[[seq_10_2], [seq_10_3], [seq_10_4], ],  # [seq_10_5], ],  # [seq_10_6]],
#                  additional_vars=["cmp", "asg"],
#                  iterations=5)
# tester.print_results()

##########################

# fast
# tester = SortPerformanceComparator()
# tester.calculate(algorithms=[ShellSort, ShellSort4, ShellSort8, HeapSortRecursive, QuickSort, MergeSort],
#                  dataset=[[seq_10_2], [seq_10_3], ],  # [seq_10_4], [seq_10_5], ],  # [seq_10_6]],
#                  additional_vars=["cmp", "asg"],
#                  iterations=20)
# tester.print_results()

##############################


# tester = SortPerformanceComparator()
# for i in range(5):  # прогоны с разными данными и усредненнием времени
#     seq_10_2 = shf(10 ** 2)
#     seq_10_3 = shf(10 ** 3)
#
#     tester.calculate(algorithms=[ShellSort, ],
#                      dataset=[[seq_10_2], [seq_10_3], ],
#                      additional_vars=["cmp", "asg"],
#                      iterations=20)
# tester.print_results()


#################################

rnd_10_2 = rnd(10**2, 999)
rnd_10_3 = rnd(10**3, 999)
rnd_10_4 = rnd(10**4, 999)
rnd_10_5 = rnd(10**5, 999)
rnd_10_6 = rnd(10**6, 999)

# very fast
tester = SortPerformanceComparator()
tester.calculate(algorithms=[BucketSort, CountingSort, RadixSort],
                 dataset=[[rnd_10_2], [rnd_10_3], [rnd_10_4], [rnd_10_5], [rnd_10_6]],
                 additional_vars=["cmp", "asg"],
                 iterations=20)
tester.print_results()

