import unittest
from . import min_queue

class MyTestCase(unittest.TestCase):
    q = min_queue.MinQueue()
    q.enqueue(25)
    q.enqueue(32)
    q.enqueue(100)
    q.enqueue(40)
    def setUp(self) -> None:
        pass
    def test_something(self):
        self.assertEqual(self.q.minimum(), 25)
        self.q.dequeue()
        self.assertEqual(self.q.minimum(), 32)
        self.q.dequeue()
        self.assertEqual(self.q.minimum(), 40)
        self.assertEqual(self.q.dequeue()[0],100)
        self.assertEqual(self.q.minimum(),40)

if __name__ == '__main__':
    unittest.main()
