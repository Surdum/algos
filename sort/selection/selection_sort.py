from base import AlgoBase
from utils import generate_random_number_sequence


class SelectionSort(AlgoBase):
    description = "Selection sort"

    def prepare_args(self, *args):
        return args

    def run(self, array):
        cmp = 0
        asg = 0
        for j in range(len(array) - 1, -1, -1):
            max_item_ind = j
            for i in range(j, -1, -1):
                cmp += 1
                if array[max_item_ind] < array[i]:
                    max_item_ind = i
            t = array[j]
            array[j] = array[max_item_ind]
            array[max_item_ind] = t
            asg += 3
        self.vars['cmp'] = cmp
        self.vars['asg'] = asg
        return array


if __name__ == '__main__':
    shuffled_array = generate_random_number_sequence(100)
    print(shuffled_array)
    sort = SelectionSort()
    sorted_array = sort.run(shuffled_array)
    print(sorted_array)
    print(sort.vars)
