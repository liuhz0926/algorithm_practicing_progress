class Solution:
    """
    DFS Memorization: DivideConquer + MemoHashMap
    TIME: O(n^2) n 为深度/层数，每个点都过了一遍，所以是n（n+1）/2 所以是n^2

    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        return self.divideConquer(triangle, 0, 0, {})

    def divideConquer(self, triangle, x, y, memo):
        '''
            函数返回从x，出发，走到最底层的最短路径值
            memo中key为tuple（x，y)， value为从x，y走道最底层的最短路径值
        '''
        if x == len(triangle):
            return 0

        # 如果找过了，就不要在找了，直接把之前找到的值返回
        if (x, y) in memo:
            return memo[(x, y)]

        # divide conquer
        left = self.divideConquer(triangle, x + 1, y, memo)
        right = self.divideConquer(triangle, x + 1, y + 1, memo)

        # 在return之后先把这次找到的最短路径值记录下来，避免之后重复搜索
        memo[(x, y)] = min(left, right) + triangle[x][y]
        return memo[(x, y)]