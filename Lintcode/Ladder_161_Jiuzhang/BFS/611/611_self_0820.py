"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

DIRECTIONS = [
    (1, 2), (-1, 2),
    (1, -2), (-1, -2),
    (2, 1), (-2, 1),
    (2, -1), (-2, -1)
]


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        if not grid or not grid[0]:
            return 0

        queue = collections.deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}

        while queue:
            curt_pt = queue.popleft()
            if curt_pt == (destination.x, destination.y):
                return distance[curt_pt]

            for dx, dy in DIRECTIONS:
                next_pt = (curt_pt[0] + dx, curt_pt[1] + dy)
                if next_pt in distance:
                    continue
                if not self.is_valid(next_pt, grid):
                    continue
                distance[next_pt] = distance[curt_pt] + 1
                queue.append(next_pt)

        return -1

    def is_valid(self, point, grid):
        n, m = len(grid), len(grid[0])

        if not (0 <= point[0] < n and 0 <= point[1] < m):
            return False

        return not grid[point[0]][point[1]]


