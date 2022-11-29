class AlgoBase:
    description = NotImplemented

    def prepare_args(self, *args):
        raise NotImplementedError

    def run(self, *args):
        raise NotImplementedError
