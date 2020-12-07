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
    def __init__(self, data=None):
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

def print_tree():
    queue = Queue()
    queue.enqueue(test.root)
    res = ""
    while len(queue) > 0:
        res += str(queue.peek()) + " "
        node = queue.dequeue()
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    return res

def delete_recursively(test, x):
    if test.root is None:
        return None
    if x < test.root.data:
        test.root.left = delete_recursively(test.root.left, x)
        return test.root
    elif x > test.root.data:
        test.root.right = delete_recursively(test.root.right, x)
        return test.root
    if test.root.left is None:
        return test.root.right
    elif test.root.right is None:
        return test.root.left
    else:
        min_key = find_min(test.root.right)
        test.root.data = min_key
        test.root.right = delete_recursively(test.root.right, min_key)
        return test.root

def find_min(test):
    if test.root.left != None:
        return find_min(test.root.left)
    else:
        return test.root



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

print(print_tree())

x = int(input("Delete element: "))
delete_recursively(test, x)

print(print_tree())


#           10
#         /    \
#        3      20
#       / \     / \
#      1   7   12  22
#       \          / \
#        2        21  24
