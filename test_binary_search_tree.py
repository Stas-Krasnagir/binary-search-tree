import unittest
#from binary_search_tree import Node
from queue import *

class TestQueue(unittest.TestCase):
    def setup(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        res = []
        count = 0
        while  count < 4:
            res += self.dequeue()
            count += 1
        if res == [1, 2, 3]:
            print("test_enqueue is OK")
        else:
            print("test_enqueue is FAIL")


    def test_dequeue(self):
        pass

    def test_is_empty(self):
        pass

    def test_peek(self):
        pass

    def test___len__(self):
        pass


class TestNode(unittest.TestCase):
    pass


class TestTree(unittest.TestCase):

    def test_insert(self):
        pass

    def test_print_tree(self):
        pass

    def test_find(self):
        pass


    def test_minimum(self):
        pass

    def test_delete_recursively(self):
        pass


if __name__ == "__main__":
    unittest.main()



