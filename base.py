import re


class AlgoBase:
    @property
    def description(self):
        words = re.findall('[A-Z][^A-Z]*', self.__class__.__name__)
        for i in range(1, len(words)):
            words[i] = words[i].lower()
        return ' '.join(words)

    def prepare_args(self, *args):
        return args

    def run(self, *args):
        raise NotImplementedError


class Sort:
    def __init__(self):
        self.vars = {'cmp': 0, 'asg': 0}

    def inc_cmp(self, value=1):
        self.vars['cmp'] += value

    def inc_asg(self, value=1):
        self.vars['asg'] += value

    def swap(self, array, i, j):
        t = array[i]
        array[i] = array[j]
        array[j] = t
        self.inc_asg(3)
