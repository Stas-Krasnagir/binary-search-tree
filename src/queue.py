class Queue:
    def __init__(self):
        self.item = []

    def enqueue(self, item: int):
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
