import typing


class Node:
    key: typing.Any
    value: typing.Any
    next: "Node" or None

    def __init__(self, key, value, next_=None):
        self.key = key
        self.value = value
        self.next = next_


class HashMap:
    def __init__(self, init_size=10):
        self._table: typing.List[Node or None] = [None for _ in range(init_size)]
        self._size = init_size
        self._length = 0

    def _get_index(self, key):
        return hash(key) % self._size

    def _find(self, key):
        current = self._table[self._get_index(key)]
        found = False
        while current is not None:
            if current.key == key:
                found = True
                break
            current = current.next
        return current if found else None

    def _resize(self):
        new_hm = HashMap(self._size * 2)
        for key, value in self.items():
            new_hm.set(key, value)
        self._table = new_hm._table
        self._size = new_hm._size

    def set(self, key, item):
        if self._length >= self._size:
            self._resize()
        index = self._get_index(key)
        if self._table[index] is None:
            self._table[index] = Node(key, item)
        else:
            node = self._find(key)
            if not node:
                self._table[index] = Node(key, item, self._table[index])
            else:
                node.value = item
        self._length += 1

    def get(self, key, default=...):
        node = self._find(key)
        if not node:
            if default is ...:
                raise KeyError('Key does not exists')
            else:
                return default
        return node.value

    def items(self):
        for index in range(self._size):
            current = self._table[index]
            while current is not None:
                yield current.key, current.value
                current = current.next

    def delete(self, key):
        index = self._get_index(key)
        prev = None
        current = self._table[index]
        found = False
        while current is not None:
            if current.key == key:
                found = True
                break
            prev = current
            current = current.next
        if found:
            if not prev:
                self._table[index] = current.next
            else:
                prev.next = current.next
                self._length -= 1


if __name__ == '__main__':
    hm = HashMap()
    hm.set("3", "world")
    hm.set("5", "world1")
    hm.set("2", "world1")
    hm.set(1, "world1")
    for k, v in hm.items():
        print(k, v)
    print()
    hm.delete('5')
    for k, v in hm.items():
        print(k, v)

