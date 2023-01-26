import typing


class FactorArray:

    array: list
    factor: int
    size: int

    def __init__(self, factor: int = 50, init_length: int = 10):
        self.factor = factor
        self.array = [None for _ in range(init_length)]
        self.size = 0

    def add(self, item: typing.Any):
        if self.size == len(self.array):
            self.resize()
        self.array[self.size] = item
        self.size += 1

    def add_by_index(self, item: typing.Any, index: int) -> None:
        if self.size == len(self.array):
            self.resize()
        self.size += 1
        new_value = item
        for i in range(index, self.size):
            old_value = self.array[i]
            self.array[i] = new_value
            new_value = old_value

    def get(self, index: int):
        return self.array[index]

    def remove(self, index: int) -> typing.Any:
        new_value = None
        for i in range(self.size - 1, index - 1, -1):
            old_value = self.array[i]
            self.array[i] = new_value
            new_value = old_value
        return new_value

    def resize(self):
        new_array = [None for _ in range(len(self.array) + len(self.array) * self.factor // 100)]
        for i, item in enumerate(self.array):
            new_array[i] = item
        self.array = new_array

    def __str__(self):
        return str(self.array)


if __name__ == '__main__':
    array = FactorArray()
    array.add(3)
    array.add(2)
    array.add(1)
    array.add(6)
    array.add(3)
    print(array)
    print('Add item 5 by index 2')
    array.add_by_index(5, 2)
    print(array)
    print('Removed element by index 4:', array.remove(4))
    print(array)
