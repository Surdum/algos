class AlgoBase:
    description = None

    def prepare_args(self, *args):
        raise NotImplementedError

    def run(self, *args):
        raise NotImplementedError
