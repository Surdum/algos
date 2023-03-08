import typing


class SingleArray:
    array: list

    def __init__(self):
        self.array = []

    def size(self):
        return len(self.array)

    def add(self, item: typing.Any):
        self.resize()
        self.array[self.size() - 1] = item

    def add_by_index(self, item: typing.Any, index: int) -> None:
        new_value = item
        for i in range(index, self.size()):
            old_value = self.array[i]
            self.array[i] = new_value
            new_value = old_value

    def get(self, index: int) -> typing.Any:
        return self.array[index]

    def remove(self, index: int) -> typing.Any:
        new_value = None
        for i in range(self.size() - 1, index - 1, -1):
            old_value = self.array[i]
            self.array[i] = new_value
            new_value = old_value
        return new_value

    def resize(self) -> None:
        new_array = [None for _ in range(self.size() + 1)]
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array

    def __str__(self):
        return str(self.array)


if __name__ == '__main__':
    array = SingleArray()
    array.add(9)
    array.add(8)
    array.add(7)
    array.add(6)
    array.add(5)
    print(array)
    print('Add item 2 by index 2')
    array.add_by_index(2, 2)
    print(array)
    print('Removed element by index 3:', array.remove(3))
    print(array)


