import unittest
from add_two_numbers import Solution
from problems.structures.list_node import create_from_list


# Input: l1 = [2,4,3], l2 = [5,6,4]
class MyTestCase(unittest.TestCase):
    def test_two_sum(self):
        s = Solution()

        self.assertEqual(s.addTwoNumbers(
            create_from_list([2, 4, 3]),
            create_from_list([5, 6, 4])),
            create_from_list([7, 0, 8]))


if __name__ == '__main__':
    unittest.main()
