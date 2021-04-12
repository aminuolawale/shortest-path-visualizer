#!usr/bin/python3
import unittest
from shortest_path import ShortestPath


class TestShortestPath(unittest.TestCase):
    def setUp(self):
        self.grid = [
            [0, 0, 0, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 0],
        ]
        self.expected_path = [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 2),
            (2, 2),
            (2, 1),
            (2, 0),
        ]

    def test_execute(self):
        shortest_path = ShortestPath(self.grid, start=(0, 0), end=(2, 0)).execute()
        self.assertEqual(shortest_path, self.expected_path)


if __name__ == "__main__":
    unittest.main()