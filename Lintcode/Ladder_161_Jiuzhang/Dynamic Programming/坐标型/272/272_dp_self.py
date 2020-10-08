class Solution:
    """
    和111几乎一样
    @param n: An integer
    @return: An Integer
    """

    def climbStairs2(self, n):
        if n <= 1:
            return 1
        if n == 2:
            return 2

        #state: 从0到i 有多少步。每一步是前三次的和，因为这次可以走1，2， 3步。所以init也要写三个。但是注意我们最好单独把他们return了
        dp = [0] * (n + 1)

        # initial:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]
