import typing


class SLLNode:
    next: "SLLNode" or None = None
    value: typing.Any

    def __init__(self, value):
        self.value = value


class SLL:
    """
    Single linked list
    """
    length = 0
    parent = None
    last_child = None

    def add(self, value, index=-1):
        if self.parent is None:
            self.parent = SLLNode(value)
            self.last_child = self.parent
            self.length += 1
        else:
            if index == -1:
                new_node = SLLNode(value)
                self.last_child.next = new_node
                self.last_child = new_node
                self.length += 1
            else:
                if index >= self.length:
                    self.add(value)
                else:
                    t = index
                    prev_node = None
                    curr_node = self.parent
                    while t > 0:
                        prev_node = curr_node
                        curr_node = curr_node.next
                        t -= 1
                    if prev_node is None:
                        new_node = SLLNode(value)
                        new_node.next = self.parent
                        self.parent = new_node
                    else:
                        new_node = SLLNode(value)
                        prev_node.next = new_node
                        new_node.next = curr_node
                    self.length += 1

    def remove(self, index):
        if index >= self.length or self.parent is None:
            return None
        if index == 0:
            value = self.parent.value
            self.parent = self.parent.next
            self.length -= 1
            return value
        prev_node = None
        curr_node = self.parent
        t = index
        while t > 0:
            prev_node = curr_node
            curr_node = curr_node.next
            t -= 1
        value = curr_node.value
        prev_node.next = curr_node.next
        if self.length - 1 == index:
            self.last_child = prev_node
        self.length -= 1
        return value

    def __iter__(self):
        curr_node = self.parent
        while curr_node is not None:
            yield curr_node.value
            curr_node = curr_node.next

    def __add__(self, other: "SLL"):
        self.last_child.next = other.parent
        self.last_child = other.last_child

    def __str__(self):
        if self.parent is None:
            return ""
        curr_node = self.parent
        s = f""
        while curr_node is not None:
            s += str(curr_node.value)
            curr_node = curr_node.next
            if curr_node is not None:
                s += ", "
        return s


class SortedSLL(SLL):
    LESS_THAN = "less than"
    GREATER_THAN = "greater than"

    def __init__(self, direction='asc'):
        assert direction in ('asc', 'desc'), "direction have to be 'asc' or 'desc'"
        self.direction = direction

    def c(self, first, sign, second):
        if self.direction == 'desc':
            if sign == self.LESS_THAN:
                sign = self.GREATER_THAN
            elif sign == self.GREATER_THAN:
                sign = self.LESS_THAN
        if sign == self.LESS_THAN:
            return first < second
        elif sign == self.GREATER_THAN:
            return first > second

    def add_with_sort(self, value):
        new_node = SLLNode(value)
        if self.parent is None or self.c(value, self.LESS_THAN, self.parent.value):
            self.add(value, 0)
        elif self.c(value, self.GREATER_THAN, self.last_child.value):
            self.last_child.next = new_node
            self.last_child = new_node
        else:
            prev_node = None
            curr_node = self.parent
            index = 0
            while self.c(value, self.GREATER_THAN, curr_node.value):
                prev_node = curr_node
                curr_node = curr_node.next
                index += 1
            prev_node.next = new_node
            new_node.next = curr_node


if __name__ == '__main__':
    sll = SLL()
    print(sll)
    sll.add(5)
    print(sll)
    sll.add(7)
    print(sll)
    sll.add(10)
    print(sll)
    sll.add(666, 0)
    print(sll)
    sll.add(777, 111)
    print(sll)

    for elem in sll:
        print(elem)
    print('remove')
    sll.remove(0)
    print(sll)
    sll.remove(1000)
    print(sll)
    sll.remove(2)
    print(sll)
    sll.remove(2)
    print(sll)
    sll.remove(0)
    print(sll)
    sll.remove(0)
    print(sll)
    sll.remove(0)
    print('a', sll)
