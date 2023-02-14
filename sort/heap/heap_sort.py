from base import AlgoBase, Sort
from utils import generate_random_number_sequence


class HeapSort(AlgoBase, Sort):
    description = "Heap sort"

    def heapify(self, array, index):
        parent_index = (index - 1) // 2
        self.inc_cmp()
        if array[index] > array[parent_index]:
            self.swap(array, index, parent_index)

    def run(self, array):
        for i in range(len(array) - 1, -1, -1):
            for j in range(i, 0, -1):
                self.heapify(array, j)
            self.swap(array, 0, i)
        return array


class HeapSortRecursive(AlgoBase, Sort):
    description = "Heap sort recursive"

    def _heapify(self, array, root, size):
        x = root
        left = 2 * x + 1
        right = left + 1
        if left < size and array[left] > array[x]:
            x = left
        if right < size and array[right] > array[x]:
            x = right
        if x == root:
            return
        self.inc_cmp(3)
        self.swap(array, root, x)
        self._heapify(array, x, size)

    def run(self, array):
        for i in range(len(array) // 2 - 1, -1, -1):
            self._heapify(array, i, len(array))
        for j in range(len(array) - 1, 0, -1):
            self.swap(array, 0, j)
            self._heapify(array, 0, j)
        return array


if __name__ == '__main__':
    shuffled_array = generate_random_number_sequence(10)
    print(shuffled_array)
    sort = HeapSort()
    sorted_array = sort.run(shuffled_array)
    print(sorted_array)
    print(sort.vars)

    shuffled_array = generate_random_number_sequence(10)
    print(shuffled_array)
    sort = HeapSortRecursive()
    sorted_array = sort.run(shuffled_array)
    print(sorted_array)
    print(sort.vars)

