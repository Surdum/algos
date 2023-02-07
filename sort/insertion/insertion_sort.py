from base import AlgoBase
from utils import generate_random_number_sequence


class InsertionSort(AlgoBase):
    description = "Insertion sort"

    def prepare_args(self, array: list):
        return array.copy()

    def run(self, array: list):
        cmp = 0
        asg = 0
        for i in range(1, len(array)):
            for j in range(i, 0, -1):
                cmp += 1
                if array[j-1] > array[j]:
                    t = array[j-1]
                    array[j-1] = array[j]
                    array[j] = t
                    asg += 3
        self.vars['cmp'] = cmp
        self.vars['asg'] = asg
        return array


class InsertionSortShift(AlgoBase):
    description = "Insertion sort shift"

    def prepare_args(self, array: list):
        return array.copy()

    def run(self, array: list):
        cmp = 0
        asg = 0
        for j in range(1, len(array)):
            t = array[j]
            asg += 1
            i = j - 1
            cmp += 1
            while i >= 0 and array[i] > t:
                cmp += 1
                array[i + 1] = array[i]
                asg += 1
                i -= 1
            array[i + 1] = t
            asg += 1

        self.vars['cmp'] = cmp
        self.vars['asg'] = asg
        return array


class InsertionSortBinary(AlgoBase):
    description = "Insertion sort binary"
    vars = {'cmp': 0, 'asg': 0}

    def prepare_args(self, array: list):
        return array.copy()

    def _binary_search(self, array, key, low, high):
        if high <= low:
            return (low + 1) if key > array[low] else low
        self.vars['cmp'] += 1
        mid = (low + high) // 2
        if key > array[mid]:
            return self._binary_search(array, key, mid + 1, high)
        else:
            return self._binary_search(array, key, low, mid - 1)

    def run(self, array: list):
        cmp = 0
        asg = 0
        for j in range(1, len(array)):
            k = array[j]
            asg += 1
            p = self._binary_search(array, k, 0, j - 1)
            i = j - 1
            while i >= p:
                array[i+1] = array[i]
                asg += 1
                i -= 1
            array[i + 1] = k
            asg += 1
        self.vars['cmp'] += cmp
        self.vars['asg'] += asg
        return array


class InsertionSortOptimized(AlgoBase):
    description = "Insertion sort optimized"

    def prepare_args(self, array: list):
        return array.copy()

    def run(self, array: list):
        cmp = 0
        asg = 0
        for i in range(1, len(array)):
            j = i
            while array[j-1] > array[j] and j > 0:
                t = array[j-1]
                array[j-1] = array[j]
                array[j] = t
                j -= 1
                cmp += 1
                asg += 3
        self.vars['cmp'] = cmp
        self.vars['asg'] = asg
        return array


if __name__ == '__main__':
    garbage_array = generate_random_number_sequence(10)
    print('garbage_array', garbage_array)
    sort = InsertionSort()
    sorted_array = sort.run(garbage_array)
    print('sorted_array', sorted_array)
    print()
    garbage_array = generate_random_number_sequence(10)
    print('garbage_array', garbage_array)
    sort = InsertionSortOptimized()
    sorted_array = sort.run(garbage_array)
    print('sorted_array', sorted_array)
    print()
    garbage_array = generate_random_number_sequence(10)
    print('garbage_array', garbage_array)
    sort = InsertionSortShift()
    sorted_array = sort.run(garbage_array)
    print('sorted_array', sorted_array)
    print()
    garbage_array = generate_random_number_sequence(10)
    print('garbage_array', garbage_array)
    sort = InsertionSortBinary()
    sorted_array = sort.run(garbage_array)
    print('sorted_array', sorted_array)
