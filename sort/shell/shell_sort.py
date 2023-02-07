from base import AlgoBase
from utils import generate_random_number_sequence


class ShellSort(AlgoBase):
    description = "Shell sort"

    def prepare_args(self, *args):
        return args

    def run(self, array):
        cmp = 0
        asg = 0
        gap = len(array) // 2
        while gap > 0:
            for i in range(gap, len(array)):
                j = i
                cmp += 1
                while j >= gap and array[j - gap] > array[j]:
                    t = array[j - gap]
                    array[j - gap] = array[j]
                    array[j] = t
                    j -= gap
                    asg += 1
            gap //= 2
        self.vars['cmp'] = cmp
        self.vars['asg'] = asg
        return array


class ShellSort4(AlgoBase):
    description = "Shell sort"

    def prepare_args(self, *args):
        return args

    def run(self, array):
        cmp = 0
        asg = 0
        gap = len(array) // 4
        while gap > 0:
            for i in range(gap, len(array)):
                j = i
                cmp += 1
                while j >= gap and array[j - gap] > array[j]:
                    t = array[j - gap]
                    array[j - gap] = array[j]
                    array[j] = t
                    j -= gap
                    asg += 1
            gap //= 2
        self.vars['cmp'] = cmp
        self.vars['asg'] = asg
        return array


class ShellSort8(AlgoBase):
    description = "Shell sort"

    def prepare_args(self, *args):
        return args

    def run(self, array):
        cmp = 0
        asg = 0
        gap = len(array) // 8
        while gap > 0:
            for i in range(gap, len(array)):
                j = i
                cmp += 1
                while j >= gap and array[j - gap] > array[j]:
                    t = array[j - gap]
                    array[j - gap] = array[j]
                    array[j] = t
                    j -= gap
                    asg += 1
            gap //= 2
        self.vars['cmp'] = cmp
        self.vars['asg'] = asg
        return array

if __name__ == '__main__':
    garbage_array = generate_random_number_sequence(10)
    print('garbage_array', garbage_array)
    sort = ShellSort()
    sorted_array = sort.run(garbage_array)
    print('sorted_array', sorted_array)



