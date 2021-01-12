class Solution:
    """
    DFS 暴力搜索法 O(2^n)
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        self.minimum = float('inf')
        self.dfs(0, 0, triangle, 0)
        return self.minimum

    def dfs(self, x, y, triangle, previous_sum):
        if x == len(triangle):
            # 前面已经从0加到了n-1
            self.minimum = min(self.minimum, previous_sum)
            return

        self.dfs(x + 1, y, triangle, previous_sum + triangle[x][y])
        self.dfs(x + 1, y + 1, triangle, previous_sum + triangle[x][y])
        