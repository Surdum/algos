from base import AlgoBase
from utils import generate_random_number_sequence


class BubbleSort(AlgoBase):
    description = "Bubble sort"

    def prepare_args(self, array: list):
        return array.copy()

    def run(self, array: list):
        cmp = 0
        asg = 0
        for i in range(len(array)):
            for j in range(len(array) - 1):
                cmp += 1
                if array[j] > array[j+1]:
                    t = array[j]
                    array[j] = array[j+1]
                    array[j+1] = t
                    asg += 3
        self.vars['cmp'] = cmp
        self.vars['asg'] = asg
        return array


class BubbleSortOptimized(AlgoBase):
    description = "Bubble sort optimized"

    def prepare_args(self, *args):
        return args

    def run(self, array):
        cmp = 0
        asg = 0
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                cmp += 1
                if array[j] > array[j+1]:
                    t = array[j]
                    array[j] = array[j+1]
                    array[j+1] = t
                    asg += 3
        self.vars['cmp'] = cmp
        self.vars['asg'] = asg
        return array


if __name__ == '__main__':
    garbage_array = generate_random_number_sequence(10)
    print('garbage_array', garbage_array)
    sort = BubbleSort()
    sorted_array = sort.run(garbage_array)
    print('sorted_array', sorted_array)
    print()
    garbage_array = generate_random_number_sequence(10)
    print('garbage_array', garbage_array)
    sort = BubbleSortOptimized()
    sorted_array = sort.run(garbage_array)
    print('sorted_array', sorted_array)

