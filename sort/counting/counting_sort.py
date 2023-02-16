from base import AlgoBase, Sort
from utils import generate_shuffled_number_sequence, generate_random_number_sequence


class CountingSort(AlgoBase, Sort):
    def run(self, array):
        max_item = array[0]
        for item in array:
            self.inc_cmp()
            if item > max_item:
                max_item = item
                self.inc_asg()
        count_array = [0 for _ in range(max_item + 1)]
        for item in array:
            count_array[item] += 1
            self.inc_asg()
        for i in range(1, len(count_array)):
            count_array[i] = count_array[i] + count_array[i - 1]
            self.inc_asg()
        new_array = [None for _ in range(len(array))]
        for i in range(len(array) - 1, -1, -1):
            item = array[i]
            count_array[item] -= 1
            new_array[count_array[item]] = item
            self.inc_asg(2)
        return new_array


if __name__ == '__main__':
    shuffled_array = generate_shuffled_number_sequence(10)
    print(shuffled_array)
    sort = CountingSort()
    sorted_array = sort.run(shuffled_array)
    print(sorted_array)

    random_array = generate_random_number_sequence(10, 20)
    print(random_array)
    sort = CountingSort()
    sorted_array = sort.run(random_array)
    print(sorted_array)


