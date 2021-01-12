from collections import deque

DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # 可以加上 or not gird[0]就是说横竖都要有才可以
        if not grid:
            return 0

        num_of_island = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j] or (i, j) in visited:
                    continue
                self.bfs(i, j, grid, visited)
                num_of_island += 1

        return num_of_island

    def bfs(self, x, y, grid, visited):
        queue = deque([(x, y)])
        # 这里漏写了 因为遇到当前grid xy是1 才会bfs，bfs这两个点也要确保visted
        visted.add((x, y))
        while queue:
            i, j = queue.popleft()
            print(i, j)
            for direct in DIRECTION:
                if not self.is_valid(i + direct[0], j + direct[1], grid, visited):
                    continue
                queue.append((i + direct[0], j + direct[1]))
                visited.add((i + direct[0], j + direct[1]))

    def is_valid(self, x, y, grid, visited):
        n, m = len(grid), len(grid[0])
        # 注意是不要等于 n和m。否则越界
        # 注意事项x不越界 或者 y不越界。
        # 或者写成不在（x和y的范围里面） if not (x and y)
        if not 0 <= x < n or not 0 <= y < m:
            return False
        if (x, y) in visited:
            return False
        return grid[x][y]