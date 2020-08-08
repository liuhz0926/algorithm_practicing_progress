class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """

    def rerange(self, A):
        # 找有多少个正的 有多少个负的
        pos = len([a for a in A if a > 0])
        neg = len(A) - pos

        # 整体先把所有的数字分开，分成一边为正 一边为负
        self.partition(A, pos > neg)
        # 然后再交换
        self.interleave(A, pos == neg)

    def partition(self, A, start_positive):
        # 第二个条件再看是左边为正还是左边为负
        # 如果正的多，左边是正的。如果负的多，左边是负
        flag = 1 if start_positive else -1
        left, right = 0, len(A) - 1
        while left <= right:
            # flag是正的，则左边要放正的。和partiion一样，如果左边放负的则flag 为-1
            while left <= right and A[left] * flag > 0:
                left += 1
            while left <= right and A[right] * flag < 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

    def interleave(self, A, has_same_length):
        # 从第二位和最后一位开始交换
        left, right = 1, len(A) - 1
        # 做交换。如果是正负的数目都相同。那就交换前面组的第二位和后面的倒数第二位开始交换
        if has_same_length:
            right = len(A) - 2

        # 每次交换都要往前移动两个，因为前面的一个都不动
        while left < right:
            A[left], A[right] = A[right], A[left]
            left, right = left + 2, right - 2
