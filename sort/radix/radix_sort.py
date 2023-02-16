from base import AlgoBase, Sort
from utils import generate_random_number_sequence


class RadixSort(AlgoBase, Sort):
    def run(self, array):
        max_item = array[0]
        for item in array:
            self.inc_cmp()
            if item > max_item:
                max_item = item
                self.inc_asg()
        max_len = len(str(max_item))
        d = 10
        curr_array = array.copy()
        temp_array = [None for _ in range(len(curr_array))]
        while d <= 10**max_len:
            count_array = [0 for _ in range(10)]
            for item in curr_array:
                digit = (item % d) // (d // 10)
                count_array[digit] += 1
            for i in range(1, len(count_array)):
                count_array[i] = count_array[i] + count_array[i - 1]
            for i in range(len(curr_array) - 1, -1, -1):
                digit = (curr_array[i] % d) // (d // 10)
                count_array[digit] -= 1
                temp_array[count_array[digit]] = curr_array[i]
                self.inc_asg(2)
            curr_array = temp_array
            temp_array = [None for _ in range(len(curr_array))]
            d *= 10
        return curr_array


if __name__ == '__main__':
    t_array = generate_random_number_sequence(10, 999)
    print(t_array)
    sort = RadixSort()
    sorted_array = sort.run(t_array)
    print(sorted_array)


