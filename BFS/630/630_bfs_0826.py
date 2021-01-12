DIRECTIONS = [
    (1, 2), (-1, 2),
    (2, 1), (-2, 1),
]


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])
        queue = collections.deque([(0, 0)])
        distance = {(0, 0): 0}

        while queue:
            x, y = queue.popleft()
            if (x, y) == (n - 1, m - 1):
                return distance[(x, y)]

            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy

                if self.is_valid(next_x, next_y, grid, distance):
                    distance[(next_x, next_y)] = distance[(x, y)] + 1
                    queue.append((next_x, next_y))

        return -1

    def is_valid(self, x, y, grid, distance):
        n, m = len(grid), len(grid[0])

        if (x, y) in distance:
            return False
        if not (0 <= x < n and 0 <= y < m):
            return False

        return not grid[x][y]
