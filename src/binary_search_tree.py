from typing import Generic, TypeVar, Optional
from src.queue import *

T = TypeVar('T')


class Node:
    def __init__(self, data):
        self.data: T = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class Tree(Generic[T]):
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, data: int) -> None:
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node: Node) -> None:
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("END")

    def print_tree(self):
        queue = Queue()
        queue.enqueue(self.root)
        res: str = ""
        while len(queue.item) > 0:
            res += str(queue.peek()) + " "
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return res

    def delete_node(self, node: Node):
        self.__delete_rec(self.root, node)

    def __minimum(self, node: Node) -> Node:
        if node.left is None:
            return node
        return self.__minimum(node.left)

    def __delete_rec(self, root: Node, x: T):
        if root is None:
            return root
        elif x < root.data:
            root.left = self.__delete_rec(root.left, x)
        elif x > root.data:
            root.right = self.__delete_rec(root.right, x)
        elif root.left is not None and root.right is not None:
            root.data = self.__minimum(root.right).data
            root.right = self.__delete_rec(root.right, root.data)
        else:
            if root.left is not None:
                root.data = root.left
            elif root.right is not None:
                root.data = root.right
            else:
                root = None
        return root



