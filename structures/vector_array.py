import typing


class VectorArray:
    array: list
    vector: int
    size: int

    def __init__(self, vector: int = 10):
        self.vector = vector
        self.array = []
        self.size = 0

    def add(self, item: typing.Any) -> None:
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

    def get(self, index: int) -> typing.Any:
        return self.array[index]

    def remove(self, index: int) -> typing.Any:
        new_value = None
        for i in range(self.size - 1, index - 1, -1):
            old_value = self.array[i]
            self.array[i] = new_value
            new_value = old_value
        return new_value

    def resize(self) -> None:
        new_array = [None for _ in range(len(self.array) + self.vector)]
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array

    def __str__(self):
        return str(self.array)


if __name__ == '__main__':
    array = VectorArray(10)
    array.add(8)
    array.add(5)
    array.add(1)
    print(array)
    print('Add item 9 by index 1')
    array.add_by_index(9, 1)
    print(array)
    print('Removed element by index 3:', array.remove(3))
    print(array)
    print('Removed element by index 1:', array.remove(1))
    print(array)

