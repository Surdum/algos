class AlgoBase:
    description = NotImplemented
    vars = {'cmp': 0, 'asg': 0}

    def prepare_args(self, *args):
        raise NotImplementedError

    def run(self, *args):
        raise NotImplementedError
