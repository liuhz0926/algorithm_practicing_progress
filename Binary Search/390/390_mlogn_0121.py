class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak

    二分法 O(mLogn)
    """

    def findPeakII(self, A):

        n, m = len(A), len(A[0])
        # 最外围一定是小的 所以从1和n-2开始
        up, down = 1, n - 2

        while up + 1 < down:
            # 找到mid的row 然后和mid 这row的最大的column index
            mid = up + (down - up) // 2
            col_max = self.find_max_col(A, mid)

            # 如果下面的比他大（+1的），则下面可能有peak，up动
            if A[mid][col_max] < A[mid + 1][col_max]:
                up = mid
            # 如果上面的比他大，则上面可能有peak，down动
            elif A[mid][col_max] < A[mid - 1][col_max]:
                down = mid
            # 上下都没有他大，说明这个就是个peak
            else:
                return (mid, col_max)

        # 出来后检查up和down找到他的最高
        up_col = self.find_max_col(A, up)
        if A[up][up_col] > A[up - 1][up_col] and A[up][up_col] > A[up + 1][up_col]:
            return (up, up_col)
        # up不是peak，查down
        down_col = self.find_max_col(A, down)
        return (down, down_col)

    # 循环找到这一行里面最大的那个column index
    def find_max_col(self, A, row_index):
        col_index = 0
        for i in range(len(A[row_index])):
            if A[row_index][i] > A[row_index][col_index]:
                col_index = i
        return col_index
