class Solution:
    """
    为什么是dp，求how many unique path，求方案总数
    自顶向下
    ij这个点可以从上面过来，也可以从左边过来，dp[i][j]代表从00走到ij的方案总数
    所以i j其实是左边和右边加起来。
    初始化：最左边都是1，最上面都是1，（第0行第0列），求最后一个点
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # state: dp[i][j]代表从0, 0走到i, j的方案总数
        dp = [[0] * n for _ in range(m)]

        # initial:初始化第0行第0列
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # function: dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # answer: 最后一个点
        return dp[m - 1][n - 1]


class Solution:
    """
    为什么是dp，求how many unique path，求方案总数
    自底向上 （其实是原来整个反过来）从当前点走到右下角的方案总数（所以右下角走到自己只有1，最下面和最右边两排都是只有1）
    i j 依赖于下面和右面，走到最右下角那个店需要经过下面和右面这个两个点
    注意loop是反过来loop的。因为是退到左上角
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # state: dp[i][j]代表从i, j走到m-1, n-1的方案总数
        dp = [[0] * n for _ in range(m)]

        # initial:初始化最下面m-1和最右面n-1
        for i in range(m):
            dp[i][n - 1] = 1
        for j in range(n):
            dp[m - 1][j] = 1

        # function: dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        # answer: 从第一个点
        return dp[0][0]

