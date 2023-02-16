from base import AlgoBase, Sort
from utils import generate_shuffled_number_sequence


class MergeSort(AlgoBase, Sort):
    description = "Merge sort"

    def _merge(self, array, left, x, right):
        array_m = [0] * (right - left + 1)
        left_ = left
        right_ = x + 1
        m = 0
        while (left_ <= x) and (right_ <= right):
            if array[left_] < array[right_]:
                array_m[m] = array[left_]
                m += 1
                left_ += 1
            else:
                array_m[m] = array[right_]
                m += 1
                right_ += 1
            self.inc_cmp()
            self.inc_asg()
        while left_ <= x:
            array_m[m] = array[left_]
            m += 1
            left_ += 1
            self.inc_asg()
        while right_ <= right:
            array_m[m] = array[right_]
            m += 1
            right_ += 1
            self.inc_asg()

        for i in range(left, right + 1):
            array[i] = array_m[i - left]

    def _merge_sort(self, array, left, right):
        self.inc_cmp()
        if left >= right:
            return
        m = (left + right) // 2
        self._merge_sort(array, left, m)
        self._merge_sort(array, m + 1, right)
        self._merge(array, left, m, right)
        return array

    def run(self, array):
        return self._merge_sort(array, 0, len(array) - 1)


if __name__ == '__main__':
    shuffled_array = generate_shuffled_number_sequence(10)
    print(shuffled_array)
    sort = MergeSort()
    sorted_array = sort.run(shuffled_array)
    print(sorted_array)
    print(sort.vars)

