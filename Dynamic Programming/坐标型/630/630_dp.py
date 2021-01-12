REVERSED_DIRECTIONS = [
    (-1, -2), (1, -2),
    (-2, -1), (2, -1)
]  # x是上下, y是左右


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])

        # state：dp[i][j]代表从0 0 到i j的最少步数
        dp = [[float('inf')] * n for _ in range(m)]

        # initialize：起点是0
        dp[0][0] = 0

        # function
        for j in range(n):  # 必须先写n，因为向右走固定
            for i in range(m):
                # 如果是barrier，直接跳过
                if grid[i][j] == 1:
                    continue
                # 然后看前一步谁最小, 注意，x是上下，y是左右，我们看前一步
                for dx, dy in REVERSED_DIRECTIONS:
                    pre_x, pre_y = i + dx, j + dy
                    # check the range:
                    if 0 <= pre_x < m and 0 <= pre_y < n:
                        # 打擂台选最小
                        dp[i][j] = min(dp[i][j], dp[pre_x][pre_y] + 1)

        # answer
        if dp[m - 1][n - 1] == float('inf'):
            return -1
        return dp[m - 1][n - 1]

