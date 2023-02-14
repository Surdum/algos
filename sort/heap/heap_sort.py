from base import AlgoBase
from utils import generate_random_number_sequence


class HeapSort(AlgoBase):
    description = "Heap sort"

    def prepare_args(self, *args):
        return args

    def heapify(self, array, index):
        parent_index = (index - 1) // 2
        self.vars['cmp'] += 1
        if array[index] > array[parent_index]:
            t = array[index]
            array[index] = array[parent_index]
            array[parent_index] = t
            self.vars['asg'] += 3

    def run(self, array):
        cmp = 0
        asg = 0
        for i in range(len(array) - 1, -1, -1):
            for j in range(i, 0, -1):
                self.heapify(array, j)
            t = array[0]
            array[0] = array[i]
            array[i] = t
            asg += 3
        self.vars['cmp'] += cmp
        self.vars['asg'] += asg
        return array


if __name__ == '__main__':
    shuffled_array = generate_random_number_sequence(100)
    print(shuffled_array)
    sort = HeapSort()
    sorted_array = sort.run(shuffled_array)
    print(sorted_array)
    print(sort.vars)

