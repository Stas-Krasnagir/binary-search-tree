import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    def setup(self):
        self.queue = Queue()

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        res = []
        count = 0
        while count < 3:
            res.append(queue.dequeue())
            count += 1
        res_1 = [1, 2, 3]
        message = "test_enqueue is FAIL"
        self.assertEqual(res, res_1, message)


    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(55)
        res = queue.dequeue()
        res_1 = 55
        message = "test_dequeue is FAIL"
        self.assertEqual(res, res_1, message)


    def test_is_empty(self):
        test = Queue()
        test.enqueue(24)
        test.enqueue("123")
        test.enqueue(14.78)
        message = "test_is_empty is FAIL"
        self.assertFalse(test.is_empty(), message)



if __name__ == "__main__":
    unittest.main()
