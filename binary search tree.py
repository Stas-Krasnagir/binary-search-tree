class Queue:
    list = []
#    def __init__(self):
#        self.list = []

    def enqueue(self, item):
        self.list.append(item)


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.data != None:
            Queue.enqueue(self, self.data)
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
        return


root = Node(15)
root.insert(10)
root.insert(20)
root.insert(22)
root.insert(3)
root.insert(7)
root.insert(21)
root.insert(12)

root.print_tree()
