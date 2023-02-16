from base import AlgoBase, Sort
from utils import generate_shuffled_number_sequence
from structures.single_linked_list import SortedSLL


class BucketSort(AlgoBase, Sort):
    description = "Bucket sort"

    def run(self, array):
        temp_array = []
        max_item = array[0]
        array_len = len(array)
        for item in array:
            temp_array.append(SortedSLL())
            self.inc_cmp()
            if item > max_item:
                max_item = item
        for item in array:
            temp_index = item * array_len // (max_item + 1)
            temp_array[temp_index].add_with_sort(item)
            self.inc_asg()
        new_array = []
        for sll in temp_array:
            for item in sll:
                new_array.append(item)
                self.inc_asg()
        return new_array


if __name__ == '__main__':
    shuffled_array = generate_shuffled_number_sequence(10)
    print(shuffled_array)
    sort = BucketSort()
    sorted_array = sort.run(shuffled_array)
    print(sorted_array)

