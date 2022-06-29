import unittest
from two_sum import Solution


class MyTestCase(unittest.TestCase):
    def test_two_sum(self):
        s = Solution()

        self.assertEqual(s.two_sum([2, 7, 4, 9], 9), [0, 1])  # add assertion here


if __name__ == '__main__':
    unittest.main()
