class AlgoBase:
    description = NotImplemented

    def prepare_args(self, *args):
        return args

    def run(self, *args):
        raise NotImplementedError


class Sort:
    vars = {'cmp': 0, 'asg': 0}

    def inc_cmp(self, value=1):
        self.vars['cmp'] += value

    def inc_asg(self, value=1):
        self.vars['asg'] += value

    def swap(self, array, i, j):
        t = array[i]
        array[i] = array[j]
        array[j] = t
        self.inc_asg(3)
