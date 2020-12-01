class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        dequeue_elem = self.list.pop(0)
        return dequeue_elem

    def is_empty(self):
        return self.list == []
 

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
        res = Queue()
        res.enqueue(self.data)
        count = 0
        while not res.is_empty() and count < 10:
            if self.left != None:
                res.enqueue(self.left)
                self.left = self.data
                tmp = res.dequeue()
                print(tmp)
            if self.right != None:
                res.enqueue(self.right)
                self.right = self.data
                tmp2 = res.dequeue()
                print(tmp2)
            count += 1






root = Node(15)
root.insert(10)
root.insert(20)
root.insert(22)
root.insert(3)
root.insert(7)
root.insert(21)
root.insert(12)

root.print_tree()
