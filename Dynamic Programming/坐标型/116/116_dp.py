class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        if not A:
            return False

        n = len(A)

        # state: dp[i] 代表能否从起点跳到坐标i
        dp = [False] * n

        # initialization: 一开始站在0这个位置一定可以
        dp[0] = True

        # function
        for i in range(1, n):
            # 看前面每一个单词能不能走过来。只要有一个能走到i 就break，把i换成true换到下一个单词
            for j in range(i):
                # 首先j是true 其次从j这个index 加上当前的值，一定要超过i
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
                    break
                # 偷懒的写法：i 已经true了因为不break，或者后面两条都成立。不是高效，因为不会break
                # dp[i] = dp[i] or dp[j] and dp[j] and (j + A[j] >= i)

        # answer 最后一步
        return dp[n - 1]



