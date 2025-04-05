import unittest
from stacking import TheTalosProblem as ttp


class TestStacking(unittest.TestCase):
    def test_get_max_height(self):
        world = ttp()
        self.assertEqual(world.get_max_height(1), 1)
        self.assertEqual(world.get_max_height(3), 2)
        self.assertEqual(world.get_max_height(5), 3)
        self.assertEqual(world.get_max_height(8), 4)
        self.assertEqual(world.get_max_height(11), 5)
        self.assertEqual(world.get_max_height(15), 6)
        self.assertEqual(world.get_max_height(20), 7)
        self.assertEqual(world.get_max_height(25), 8)
        self.assertEqual(world.get_max_height(31), 9)
        self.assertEqual(world.get_max_height(0), -1)
        self.assertEqual(world.get_max_height(-1), -1)

    def test_get_min_boxes(self):
        world = ttp()
        self.assertEqual(world.get_min_boxes(1), 1)
        self.assertEqual(world.get_min_boxes(2), 3)
        self.assertEqual(world.get_min_boxes(3), 5)
        self.assertEqual(world.get_min_boxes(4), 8)
        self.assertEqual(world.get_min_boxes(5), 11)
        self.assertEqual(world.get_min_boxes(6), 15)
        self.assertEqual(world.get_min_boxes(7), 20)
        self.assertEqual(world.get_min_boxes(8), 25)
        self.assertEqual(world.get_min_boxes(9), 31)
        self.assertEqual(world.get_min_boxes(0), -1)
        self.assertEqual(world.get_min_boxes(-1), -1)


if __name__ == "__main__":
    unittest.main()
