from base import AlgoBase, Sort
from utils import generate_random_number_sequence


class SelectionSort(AlgoBase, Sort):
    description = "Selection sort"

    def prepare_args(self, *args):
        return args

    def run(self, array):
        for j in range(len(array) - 1, -1, -1):
            max_item_ind = j
            for i in range(j, -1, -1):
                self.inc_cmp()
                if array[max_item_ind] < array[i]:
                    max_item_ind = i
            self.swap(array, j, max_item_ind)
        return array


if __name__ == '__main__':
    shuffled_array = generate_random_number_sequence(100)
    print(shuffled_array)
    sort = SelectionSort()
    sorted_array = sort.run(shuffled_array)
    print(sorted_array)
    print(sort.vars)
