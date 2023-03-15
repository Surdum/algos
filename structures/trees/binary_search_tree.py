from structures.trees.base import Tree, Node


class BinarySearchTree(Tree):

    def insert(self, x: int) -> None:
        if self.root is None:
            self.root = Node(x)
            return
        node = self.root
        prev_node = None
        while node is not None and node.key != x:
            prev_node = node
            if x < node.key:
                node = node.left
            elif x > node.key:
                node = node.right
        if prev_node and x < prev_node.key:
            prev_node.left = Node(x)
        elif prev_node and x > prev_node.key:
            prev_node.right = Node(x)

    def search(self, x: int) -> bool:
        if self.root is None:
            return False
        node = self.root
        while node.key != x or node is not None:
            if x < node.key:
                node = node.left
            elif x > node.key:
                node = node.right
        return bool(node)

    def min_value_node(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _remove(self, x: int, elem: Node):
        if x < elem.key:
            elem.left = self._remove(x, elem.left)
        elif x > elem.key:
            elem.right = self._remove(x, elem.right)
        else:
            if elem.left is None:
                temp = elem.right
                return temp

            elif elem.right is None:
                temp = elem.left
                return temp

            temp = self.min_value_node(elem.right)
            elem.key = temp.key
            elem.right = self._remove(temp.key, elem.right)

        return elem

    def remove(self, key: int) -> None:
        self._remove(key, self.root)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(2)
    bst.insert(5)
    bst.insert(16)
    bst.insert(25)
    bst.insert(3)
    bst.insert(8)
    bst.insert(9)
    bst.insert(1000)
    bst.insert(6)
    bst.insert(1)
    bst.insert(15)
    bst.insert(999)
    bst.print()

    print('Remove 5 and 16')
    bst.remove(5)
    bst.remove(16)
    bst.print()


