class Node:
    value: str
    next: "Node" = None
    child: "Node" = None
    end: bool

    def __init__(self, value, end=False):
        self.value = value
        self.end = end


class Trie:
    parent = None

    def insert(self, word: str) -> None:
        if not self.parent:
            self.parent = Node("")
        current = self.parent
        last_index = len(word) - 1
        for i, letter in enumerate(word):
            if current.child is None:
                current.child = Node(letter, i == last_index)
                current = current.child
            else:
                current = current.child
                while current.value != letter and current.next:
                    current = current.next
                if current.value != letter:
                    current.next = Node(letter)
                    current = current.next
                if i == last_index:
                    current.end = True

    def __search(self, word):
        if not self.parent or not self.parent.child:
            return None
        current = self.parent.child
        last_index = len(word) - 1
        for i, letter in enumerate(word):
            if not current:
                return None
            while current.value != letter and current.next:
                current = current.next
            if current.value == letter:
                if i != last_index:
                    current = current.child
            else:
                return None
        return current

    def search(self, word):
        node = self.__search(word)
        return bool(node and node.end)

    def startsWith(self, prefix):
        node = self.__search(prefix)
        return bool(node)


if __name__ == '__main__':
    trie = Trie()
    trie.insert("hello")
    print(trie.search("hell"))
    print(trie.search("helloa"))
    print(trie.search("hello"))
    print(trie.startsWith("hell"))
    print(trie.startsWith("helloa"))
    print(trie.startsWith("hello"))



