#!usr/bin/python3
from queue import SimpleQueue as Queue
from typing import List, Tuple

Coord = Tuple[int, int]


class ShortestPath:
    def __init__(self, grid: List[List[int]], start: Coord, end: Coord) -> None:
        self.grid = grid
        self.start = start
        self.end = end
        self.rows = len(grid)
        self.cols = len(grid[0])
        grid_size = self.rows * self.cols
        self.visited = [False for _ in range(grid_size)]
        self.ancestors = [None for _ in range(grid_size)]
        self.q = Queue()

    def breadth_first_search(self) -> List[int]:
        self.q.put(self.start)
        index = self.coordinate_to_index(self.start)
        self.visited[index] = True
        while not self.q.empty():
            position = self.q.get()
            neighbors = self.neighbors(position)
            for neighbor in neighbors:
                index = self.coordinate_to_index(neighbor)
                if self.grid[neighbor[0]][neighbor[1]] != 1 and not self.visited[index]:
                    self.q.put(neighbor)
                    self.visited[index] = True
                    self.ancestors[index] = position

    def build_path(self) -> List[Coord]:
        iterator = self.end
        path = [iterator]
        while iterator != self.start:
            index = self.coordinate_to_index(iterator)
            ancestor = self.ancestors[index]
            path.append(ancestor)
            iterator = ancestor
        return list(reversed(path))

    def neighbors(self, coord: Coord) -> List[Coord]:
        result = []
        offset_vectors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for vector in offset_vectors:
            if (
                -1 < coord[0] + vector[0] < self.rows
                and -1 < coord[1] + vector[1] < self.cols
            ):
                result.append((coord[0] + vector[0], coord[1] + vector[1]))
        return result

    def execute(self) -> List[Coord]:
        self.breadth_first_search()
        return self.build_path()

    def coordinate_to_index(self, coord: Coord) -> int:
        return coord[0] * self.cols + coord[1]