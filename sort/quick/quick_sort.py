from base import AlgoBase, Sort
from utils import generate_shuffled_number_sequence


class QuickSort(AlgoBase, Sort):
    description = "Quick sort"

    def _split(self, array, left, right):
        p = array[right]
        m = left - 1
        j = left
        self.inc_cmp()
        while j <= right:
            self.inc_cmp()
            if array[j] <= p:
                m += 1
                self.swap(array, m, j)
            j += 1
        return m

    def _quick_sort(self, array, left, right):
        self.inc_cmp()
        if left >= right:
            return array
        m = self._split(array, left, right)
        self._quick_sort(array, left, m - 1)
        self._quick_sort(array, m + 1, right)
        return array

    def run(self, array):
        return self._quick_sort(array, 0, len(array) - 1)


if __name__ == '__main__':
    shuffled_array = generate_shuffled_number_sequence(10)
    print(shuffled_array)
    sort = QuickSort()
    sorted_array = sort.run(shuffled_array)
    print(sorted_array)
    print(sort.vars)
