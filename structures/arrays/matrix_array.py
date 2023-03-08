from single_array import SingleArray
from vector_array import VectorArray
import typing


class MatrixArray:
    size: int
    vector: int
    array: SingleArray

    def __init__(self, vector: int = 10):
        self.vector = vector
        self.array = SingleArray()
        self.size = 0

    def add(self, item: typing.Any) -> None:
        if self.size == self.array.size() * self.vector:
            self.array.add(VectorArray(self.vector))
        self.array.get(self.size // self.vector).add(item)
        self.size += 1

    def add_by_index(self, item: typing.Any, index: int) -> None:
        if self.size == self.array.size() * self.vector:
            self.array.add(VectorArray(self.vector))
        self.size += 1
        new_value = item
        for i in range(index, self.size):
            if self.array.get(i // self.vector).size == 0:
                self.array.get(i // self.vector).add(new_value)
            else:
                old_value = self.get(i)
                self.set(new_value, i)
                new_value = old_value

    def get(self, index: int) -> typing.Any:
        return self.array.get(index // self.vector).get(index % self.vector)

    def set(self, item: typing.Any, index: int) -> None:
        self.array.get(index // self.vector).array[index % self.vector] = item

    def remove(self, index: int):
        self.size -= 1
        new_value = None
        for i in range(self.size, index - 1, -1):
            old_value = self.get(i)
            self.set(new_value, i)
            new_value = old_value
        return new_value

    def __str__(self):
        # return '\n'.join([str(line) for line in self.array.array])
        return '\n'.join([' '.join([str(elem).rjust(4, ' ') for elem in line.array]) for line in self.array.array])


if __name__ == '__main__':
    array = MatrixArray(3)
    array.add(5)
    array.add(6)
    array.add(7)
    array.add(8)
    print(array)
    print()
    print('Get element by index 3:', array.get(3))
    print()
    print('Add item -1 by index 2:')
    array.add_by_index(-1, 2)
    print(array)
    print()
    print('Add item 66 by index 3:')
    array.add_by_index(66, 3)
    print(array)
    print()
    print('Add item 11 by index 5:')
    array.add_by_index(11, 5)
    print(array)
    print()
    print('Remove item by index 4:', array.remove(4))
    print(array)
