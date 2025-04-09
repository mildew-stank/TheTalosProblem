import unittest
from stacking import Solution


class TestStacking(unittest.TestCase):
    def test_get_max_height(self):
        stack = Solution()
        self.assertEqual(stack.get_max_height(1), 1)
        self.assertEqual(stack.get_max_height(3), 2)
        self.assertEqual(stack.get_max_height(5), 3)
        self.assertEqual(stack.get_max_height(8), 4)
        self.assertEqual(stack.get_max_height(11), 5)
        self.assertEqual(stack.get_max_height(15), 6)
        self.assertEqual(stack.get_max_height(20), 7)
        self.assertEqual(stack.get_max_height(25), 8)
        self.assertEqual(stack.get_max_height(31), 9)
        self.assertEqual(stack.get_max_height(0), 0)
        self.assertEqual(stack.get_max_height(-1), 0)

    def test_get_min_boxes(self):
        stack = Solution()
        self.assertEqual(stack.get_min_blocks(1), 1)
        self.assertEqual(stack.get_min_blocks(2), 3)
        self.assertEqual(stack.get_min_blocks(3), 5)
        self.assertEqual(stack.get_min_blocks(4), 8)
        self.assertEqual(stack.get_min_blocks(5), 11)
        self.assertEqual(stack.get_min_blocks(6), 15)
        self.assertEqual(stack.get_min_blocks(7), 20)
        self.assertEqual(stack.get_min_blocks(8), 25)
        self.assertEqual(stack.get_min_blocks(9), 31)
        self.assertEqual(stack.get_min_blocks(0), 0)
        self.assertEqual(stack.get_min_blocks(-1), 0)


if __name__ == "__main__":
    unittest.main()
