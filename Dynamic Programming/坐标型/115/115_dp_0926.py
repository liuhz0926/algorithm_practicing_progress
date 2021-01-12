class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        # 初始化条件：注意如果有一个barrier，那后面的点都不能reach 到了，所以都是0，那就直接break
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        # function两个条件:如果遇到barrier，说明这个路不通，说明没有方案，所以是0，其余为左边和上面的和
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
