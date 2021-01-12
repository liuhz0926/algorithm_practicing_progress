class Solution:
    """
    记忆化搜索，因为是O(n)时间，所以容易stackoverflow。
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """

    def canWinBash(self, n):
        return self.memo_search(n, {})

    def memo_search(self, n, memo):
        # 还剩下三个的时候 那就获胜了
        if n <= 3:
            return True
        # 这里用memo是因为可能这次扣1和2，另外扣3，其实都是走道同样的一个结果，所以我们要记录
        if n in memo:
            return memo[n]

        # i 取123的时候
        for i in range(1, 4):
            # 看对方是不是输了：
            if not self.memo_search(n - i, memo):
                # 记录当前是这边赢了
                memo[n] = True
                return True
        # 如果123都试完了都是对方赢，那就是这边输了
        memo[n] = False
        return False