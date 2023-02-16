from base import AlgoBase, Sort
from utils import generate_shuffled_number_sequence


class InsertionSort(AlgoBase, Sort):
    description = "Insertion sort"

    def run(self, array: list):
        for i in range(1, len(array)):
            for j in range(i, 0, -1):
                self.inc_cmp()
                if array[j-1] > array[j]:
                    self.swap(array, j, j-1)
        return array


class InsertionSortShift(AlgoBase, Sort):
    description = "Insertion sort shift"

    def run(self, array: list):
        for j in range(1, len(array)):
            t = array[j]
            i = j - 1
            self.inc_asg()
            self.inc_cmp()
            while i >= 0 and array[i] > t:
                self.inc_cmp()
                array[i + 1] = array[i]
                self.inc_asg()
                i -= 1
            array[i + 1] = t
            self.inc_asg()
        return array


class InsertionSortBinary(AlgoBase, Sort):
    description = "Insertion sort binary"

    def _binary_search(self, array, key, low, high):
        self.inc_cmp()
        if high <= low:
            return (low + 1) if key > array[low] else low
        mid = (low + high) // 2
        self.inc_cmp()
        if key > array[mid]:
            return self._binary_search(array, key, mid + 1, high)
        else:
            return self._binary_search(array, key, low, mid - 1)

    def run(self, array: list):
        for j in range(1, len(array)):
            k = array[j]
            self.inc_asg()
            p = self._binary_search(array, k, 0, j - 1)
            i = j - 1
            self.inc_cmp()
            while i >= p:
                self.inc_cmp()
                array[i+1] = array[i]
                self.inc_asg()
                i -= 1
            array[i + 1] = k
            self.inc_asg()
        return array


class InsertionSortOptimized(AlgoBase, Sort):
    description = "Insertion sort optimized"

    def run(self, array: list):
        for i in range(1, len(array)):
            j = i
            while array[j-1] > array[j] and j > 0:
                self.swap(array, j, j-1)
                j -= 1
                self.inc_cmp()
        return array


if __name__ == '__main__':
    garbage_array = generate_shuffled_number_sequence(10)
    print('garbage_array', garbage_array)
    sort = InsertionSort()
    sorted_array = sort.run(garbage_array)
    print('sorted_array', sorted_array)
    print()
    garbage_array = generate_shuffled_number_sequence(10)
    print('garbage_array', garbage_array)
    sort = InsertionSortOptimized()
    sorted_array = sort.run(garbage_array)
    print('sorted_array', sorted_array)
    print()
    garbage_array = generate_shuffled_number_sequence(10)
    print('garbage_array', garbage_array)
    sort = InsertionSortShift()
    sorted_array = sort.run(garbage_array)
    print('sorted_array', sorted_array)
    print()
    garbage_array = generate_shuffled_number_sequence(10)
    print('garbage_array', garbage_array)
    sort = InsertionSortBinary()
    sorted_array = sort.run(garbage_array)
    print('sorted_array', sorted_array)
