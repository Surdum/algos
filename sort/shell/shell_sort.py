from base import AlgoBase, Sort
from utils import generate_shuffled_number_sequence


class ShellSort(AlgoBase, Sort):
    description = "Shell sort"
    delimiter = 2

    def run(self, array):
        gap = len(array) // self.delimiter
        while gap > 0:
            for i in range(gap, len(array)):
                j = i
                self.inc_cmp()
                while j >= gap and array[j - gap] > array[j]:
                    self.swap(array, j, j - gap)
                    j -= gap
            gap //= 2
        return array


class ShellSort4(ShellSort):
    description = "Shell sort 4"
    delimiter = 4

    def run(self, array):
        return super().run(array)


class ShellSort8(ShellSort):
    description = "Shell sort 8"
    delimiter = 8

    def run(self, array):
        return super().run(array)


if __name__ == '__main__':
    garbage_array = generate_shuffled_number_sequence(10)
    print('garbage_array', garbage_array)
    sort = ShellSort()
    sorted_array = sort.run(garbage_array)
    print('sorted_array', sorted_array)



