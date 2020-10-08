class Solution:
    """
    DFS Divide Conquer O(2^n)

    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        return self.divideConquer(triangle, 0, 0)

    def divideConquer(self, triangle, x, y):
        if x == len(triangle):
            return 0

        left = self.divideConquer(triangle, x + 1, y)
        right = self.divideConquer(triangle, x + 1, y + 1)
        # 选左右最小的加上当前点
        return min(left, right) + triangle[x][y]
    