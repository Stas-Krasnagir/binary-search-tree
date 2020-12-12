from queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
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
        res = ""
        while len(queue) > 0:
            res += str(queue.peek()) + " "
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return res

    def minimum(self, root):
        if self.root.left is None:
            return root
        return self.minimum(self, root.left)

    def delete_recursively(self, x):
        if self.root is None:
            return None
        elif x < self.root.data:
            self.root.left = self.delete_recursively(self.root.left, x)
        elif x > self.root.data:
            self.root.right = self.delete_recursively(self.root.right, x)
        else:
            if self.root.left is None and self.root.right is None:
                self.root.data = None
            if self.root.left is None:
                temp = root.right
                self.root.data = None
                return temp
            elif self.root.right is None:
                temp = root.left
                self.root.data = None
                return temp
        return root

#           10
#         /    \
#        3      20
#       / \     / \
#      1   7   12  22
#       \          / \
#        2        21  24
