import unittest
from binary_search_tree import *
from queue import *

class TestTree(unittest.TestCase):

    def test_insert_and_print_tree(self):
        test = Tree()
        test.insert(10)
        test.insert(5)
        test.insert(15)

        res = ""
        queue = Queue()
        queue.enqueue(test.root)

        while len(queue) > 0:
            res += str(queue.peek()) + " "
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        if res == "10 5 15 ":
            print("test_insert is OK")
        else:
            print("test_insert is FAIL")

    def test_minimum(self):
        test = Tree()
        test.insert(10)
        test.insert(5)
        test.insert(15)
        test.insert(3)

        print(test.minimum())

    def test_delete_recursively(self):
        pass


if __name__ == "__main__":
    unittest.main()



