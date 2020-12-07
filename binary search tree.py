class Queue:
    def __init__(self):
        self.item = []

    def enqueue(self, item):
        self.item.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.item.pop()

    def is_empty(self):
        return len(self.item) == 0

    def peek(self):
        if not self.is_empty():
            return self.item[-1].data

    def __len__(self):
        return len(self.item)


class Node:
    """
    Class Node
    """

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """

    def __init__(self):
        """
        Utility function to create a root.
        """
        self.root = None

    def insert(self, data):
        """
        Insert function will insert a data into tree.
        """
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
        """
        This function will print tree.
        """
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

    def find_min(self, root):
        if self.root.left is not None:
            return self.find_min(root.left)
        else:
            return self.root

    def delete_recursively(self, root, delete_root):
        """
        Delete function will delete a node into tree.
        """
        if root is None:
            return None
        if delete_root < root.data:
            root.left = self.delete_recursively(root.left, delete_root)
        elif delete_root > root.data:
            root.right = self.delete_recursively(root.right, delete_root)
        else:
            if root.left is None and root.right is None:
                del root
            if root.left is None:
                temp = root.right
                del root
                return temp
            elif root.right is None:
                temp = root.left
                del root
                return temp
        return root


#        if self.root is None:
#            return self.root
#        if delete_root < self.root.data:
#            self.root.left = self.delete_recursively(self.root.left, delete_root)
#        elif delete_root > self.root.data:
#            self.root.right = self.delete_recursively(self.root.right, delete_root)
#            return self.root
#        if self.root.left is None:
#            return self.root.right
#        elif self.root.right is None:
#            return self.root.left
#        else:
#            min_key = self.find_min(self.root.right).data
#            self.root.data = min_key
#            self.root.right = self.delete_recursively(self.root.right, min_key)
#            return self.root


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

delete_root = int(input("Delete element: "))
test.delete_recursively(root, delete_root)

print(test.print_tree())

#           10
#         /    \
#        3      20
#       / \     / \
#      1   7   12  22
#       \          / \
#        2        21  24
