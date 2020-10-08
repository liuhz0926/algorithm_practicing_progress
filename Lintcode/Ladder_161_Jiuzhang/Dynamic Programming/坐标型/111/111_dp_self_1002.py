class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # 如果n是0其实都不用走。所以是0
        if not n:
            return 0
        if n == 1:
            return 1

        # state: 从0到i格走到的步骤有多少种方法，注意这里需要记录第0个起始点
        dp = [0] * (n + 1)

        # initial: 从0走到1有一种方法，走一步，从0走到2有两种，两次一步，一次两步
        dp[1] = 1
        dp[2] = 2

        # function：走到第i格，我们可以从i-1 走一步或者i-2走两步。所以是他们两个的步骤的综合
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # result：返回最后的结果
        return dp[n]
