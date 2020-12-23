import unittest
from src.binary_search_tree import *
from src.queue import *


class TestTree(unittest.TestCase):

    def test_insert_and_print_tree(self):
        tree = Tree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        res = ""
        queue_for_test = Queue()
        queue_for_test.enqueue(tree.root)

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
        tree = Tree()
        tree.insert(10)
        tree.insert(3)
        tree.insert(20)
        tree.insert(12)
        tree.insert(22)
        tree.insert(21)
        tree.insert(24)
        tree.insert(1)
        tree.insert(2)
        tree.insert(7)
        tree.delete_node(20)

        res = "10 3 21 1 7 12 22 2 24 "
        message = "test_delete_node is FAIL"
        self.assertEqual(tree.print_tree(), res, message)


if __name__ == "__main__":
    unittest.main()
