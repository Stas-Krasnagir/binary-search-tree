import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    def setup(self):
        self.queue = Queue()

    def test_enqueue(self):
        T = Queue()
        T.enqueue(1)
        T.enqueue(2)
        T.enqueue(3)
        res = []
        count = 0
        while count < 3:
            res.append(T.dequeue())
            count += 1
        if res == [1, 2, 3]:
            print("test_enqueue is OK")
        else:
            print("test_enqueue is FAIL")

    def test_dequeue(self):
        Q = Queue()
        Q.enqueue(55)
        if Q.dequeue() == 55:
            print("test_dequeue is OK")
        else:
            print("test_dequeue is FAIL")


    def test_is_empty(self):
        Z = Queue()
        Z.enqueue(24)
        Z.enqueue("123")
        Z.enqueue(14.78)
        if Z.is_empty() is False:
            print("est_is_empty is OK")
        else:
            print("est_is_empty is FAIL")


    def test_peek(self):
        K = Queue()
        K.enqueue(1)
        K.enqueue(2)
        K.enqueue(3)
        res = [K.peek]
        print(res)


if __name__ == "__main__":
    unittest.main()
