import typing


class Node:
    value: typing.Any
    prev: 'Node' = None
    next: 'Node' = None

    def __init__(self, value):
        self.value = value


class Queue:
    _head: Node = None
    _tail: Node = None
    length = 0

    def enqueue(self, value):
        if self._head is None:
            self._head = Node(value)
            self._tail = self._head
        else:
            new_node = Node(value)
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        self.length += 1

    def dequeue(self):
        if self._head is None:
            return None
        value = self._head.value
        if self._head.next is not None:
            self._head = self._head.next
            self._head.prev = None
        else:
            self._head = None
            self._tail = None
        self.length -= 1
        return value

    def __len__(self):
        return self.length

    def __str__(self):
        if self._head is None:
            return "no elements yet"
        s = "values "
        current_node = self._head
        while current_node.next is not None:
            s += f"{current_node.value}, "
            current_node = current_node.next
        s += f"{current_node.value}"
        return s


#######################
class PriorityNode:
    priority: int
    queue: Queue = None
    prev: 'PriorityNode' = None
    next: 'PriorityNode' = None

    def __init__(self, priority):
        self.priority = priority

    def enqueue(self, item):
        if self.queue is None:
            self.queue = Queue()
        self.queue.enqueue(item)

    def dequeue(self):
        if self.queue is None:
            return None
        return self.queue.dequeue()


class PriorityQueue:
    _head: PriorityNode = None
    _tail: PriorityNode = None

    def enqueue(self, priority: int, item: typing.Any):
        if self._head is None:
            self._head = PriorityNode(priority)
            self._head.enqueue(item)
            self._tail = self._head
        else:
            if priority > self._head.priority:
                new_node = PriorityNode(priority)
                new_node.enqueue(item)
                self._head.prev = new_node
                new_node.next = self._head
                self._head = new_node
            elif priority < self._tail.priority:
                new_node = PriorityNode(priority)
                new_node.enqueue(item)
                self._tail.next = new_node
                new_node.prev = self._tail
                self._tail = new_node
            else:
                current_node = self._head
                while current_node.priority > priority:
                    current_node = current_node.next
                if current_node.priority == priority:
                    current_node.enqueue(item)
                else:
                    new_node = PriorityNode(priority)
                    new_node.enqueue(item)
                    new_node.next = current_node
                    new_node.prev = current_node.prev
                    current_node.prev.next = new_node
                    current_node.prev = new_node

    def dequeue(self, priority=None):
        if priority is None:
            priority = self._head.priority
        current_node = self._head
        result_item = None
        while current_node.next is not None:
            if current_node.priority == priority:
                result_item = current_node.queue.dequeue()
                if len(current_node.queue) == 0:
                    if current_node.prev is not None and current_node.next is not None:
                        current_node.next.prev = current_node.prev
                        current_node.prev.next = current_node.next
                    elif current_node.prev is None:
                        current_node.next.prev = None
                        self._head = current_node.next
                    elif current_node.next is None:
                        current_node.prev.next = None
                        self._tail = current_node.prev
                    else:
                        self._head = None
                        self._tail = None
                break
            current_node = current_node.next
        return result_item

    def __str__(self):
        if self._head is None:
            return "no elements yet"
        s = ""
        current_node = self._head
        while current_node.next is not None:
            s += f"priority {current_node.priority} | {str(current_node.queue)}\n"
            current_node = current_node.next
        s += f"priority {current_node.priority} | {str(current_node.queue)}\n"
        return s


if __name__ == '__main__':
    prior_queue = PriorityQueue()
    print('Add values with different priorities')
    prior_queue.enqueue(1, 10)
    prior_queue.enqueue(1, 11)
    prior_queue.enqueue(7, 12)
    prior_queue.enqueue(5, 13)
    prior_queue.enqueue(2, 34)
    prior_queue.enqueue(6, 1)
    prior_queue.enqueue(5, 1)
    print(prior_queue)

    print('Dequeue by max priority returns', prior_queue.dequeue())
    print(prior_queue)

    print('Dequeue by priority = 2 returns', prior_queue.dequeue(2))
    print(prior_queue)

