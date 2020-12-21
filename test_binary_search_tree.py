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

        message = "test_insert is FAIL"
        res_1 = "10 5 15 "
        self.assertEqual(res, res_1, message)


    def test_delete_node(self):
        Test = Tree()
        Test.insert(10)
        Test.insert(3)
        Test.insert(20)
        Test.insert(12)
        Test.insert(22)
        Test.insert(21)
        Test.insert(24)
        Test.insert(1)
        Test.insert(2)
        Test.insert(7)
        Test.delete_node(20)

        res = "10 3 21 1 7 12 22 2 24 "
        message = "test_delete_node is FAIL"
        self.assertEqual(Test.print_tree(), res, message)





if __name__ == "__main__":
    unittest.main()



