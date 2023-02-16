from base import AlgoBase, Sort
from utils import generate_shuffled_number_sequence


class BubbleSort(AlgoBase, Sort):
    description = "Bubble sort"

    def run(self, array: list):
        for i in range(len(array)):
            for j in range(len(array) - 1):
                self.inc_cmp()
                if array[j] > array[j+1]:
                    self.swap(array, j, j+1)
        return array


class BubbleSortOptimized(AlgoBase, Sort):
    description = "Bubble sort optimized"

    def run(self, array):
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                self.inc_cmp()
                if array[j] > array[j+1]:
                    self.swap(array, j, j+1)
        return array


if __name__ == '__main__':
    garbage_array = generate_shuffled_number_sequence(10)
    print('garbage_array', garbage_array)
    sort = BubbleSort()
    sorted_array = sort.run(garbage_array)
    print('sorted_array', sorted_array)
    print()
    garbage_array = generate_shuffled_number_sequence(10)
    print('garbage_array', garbage_array)
    sort = BubbleSortOptimized()
    sorted_array = sort.run(garbage_array)
    print('sorted_array', sorted_array)

