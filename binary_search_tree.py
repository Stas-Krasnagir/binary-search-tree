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


    def find(self, data):
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif data < node.data and node.left is not None:
            self._find(data, node.left)
        elif data > node.data and node.right is not None:
            self._find(data, node.right)


    def minimum(self, root):
        if self.root.left is None:
            return root
        return self.minimum(self, root.left)


    def delete_recursively(self, x):
        if root is None:
            return None
        if x < root.data:
            root.left = self.delete_recursively(root.left, x)
        elif x > root.data:
            root.right = self.delete_recursively(root.right, x)
        else:
            if root.left is None and root.right is None:
                root.data = None
            if root.left is None:
                temp = root.right
                root.data = None
                return temp
            elif root.right is None:
                temp = root.left
                root.data = None
                return temp
        return root


test = Tree()
test.insert(10)
test.insert(20)
test.insert(22)
test.insert(3)
test.insert(7)
test.insert(21)
test.insert(12)
test.insert(1)
test.insert(2)
test.insert(24)


print(test.print_tree())
x = int(input("Delete element: "))
test.delete_recursively(x)
print(test.print_tree())

#           10
#         /    \
#        3      20
#       / \     / \
#      1   7   12  22
#       \          / \
#        2        21  24
