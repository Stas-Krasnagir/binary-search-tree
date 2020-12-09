from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


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
                cur_node.parent = cur_node.left
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
                cur_node.parent = cur_node.right
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


    def next(self, root):
        if root.right is not None:
            return self.minimum(root.right)
        y = self.root.parent
        while y is not None and self.root == y.right:
            self.root = y
            y = y.parent
        return y

    def delete(self, x):
        pass
        p = x.parent
        if x.left is None and x.right is None:
            if p.left == x:
                p.left = None
            if p.right == x:
                p.right = None
        elif x.left is None or x.right is None:
            if x.left is None:
                if p.left == x:
                    p.left = x.right
                else:
                    p.right = x.right
                x.right.parent = p
            else:
                if p.left == x:
                    p.left = x.left
                else:
                    p.right = x.left
                x.left.parent = p
        else:
            successor = next(x, t)
            x.data = successor.data
            if successor.parent.left == successor:
                successor.parent.left = successor.right
                if successor.right != null:
                    successor.right.parent = successor.parent
            else:
                successor.parent.right = successor.left
                if successor.left != null:
                    successor.right.parent = successor.parent

    def delete_recursion(self, x):
        if self.root.data == x:
            if self.root.left in None and self.root.right is None:
                self.root.data = None
            if self.root.left is not None and self.root.right is None:
                self.root.data = self.root.left
            if self.root.right is not None and self.root.left is None:
                self.root.data = self.root.right
        else:
            print("___")


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
test.delete(x)

test.delete_recursion(x)

print(test.print_tree())

#           10
#         /    \
#        3      20
#       / \     / \
#      1   7   12  22
#       \          / \
#        2        21  24
