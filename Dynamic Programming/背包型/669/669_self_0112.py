class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """

    def coinChange(self, coins, amount):
        if not coins or amount < 0:
            return -1

        # dp[i]表示总金额为i是最少的硬币数量
        dp = [float('inf')] * (amount + 1)

        # initialization
        dp[0] = 0

        for i in range(len(dp)):
            # 打擂台求看没选择一个coin的前一步的数量+1，取最小，注意界限
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]


