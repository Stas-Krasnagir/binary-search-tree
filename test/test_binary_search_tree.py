import unittest
from src.binary_search_tree import *
from src.queue import *


class TestTree(unittest.TestCase):

    def test_insert_and_print_tree(self):
        test = Tree()
        test.insert(10)
        test.insert(5)
        test.insert(15)
        res = ""
        queue_for_test = Queue()
        queue_for_test.enqueue(test.root)

        while len(queue_for_test) > 0:
            res += str(queue_for_test.peek()) + " "
            node = queue_for_test.dequeue()
            if node.left:
                queue_for_test.enqueue(node.left)
            if node.right:
                queue_for_test.enqueue(node.right)

        message = "test_insert is FAIL"
        res_1 = "10 5 15 "
        self.assertEqual(res, res_1, message)

    def test_delete_node(self):
        test = Tree()
        test.insert(10)
        test.insert(3)
        test.insert(20)
        test.insert(12)
        test.insert(22)
        test.insert(21)
        test.insert(24)
        test.insert(1)
        test.insert(2)
        test.insert(7)
        test.delete_node(20)

        res = "10 3 21 1 7 12 22 2 24 "
        message = "test_delete_node is FAIL"
        self.assertEqual(test.print_tree(), res, message)


if __name__ == "__main__":
    unittest.main()
