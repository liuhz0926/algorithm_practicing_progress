class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        if not L:
            return 0
        # 按答案的话，这个end 要是写成min(maxL, sumL //k) 如果sumL<k, 那end就会得0，一定不能得0，因为我们不要切0的长度
        start, end = 1, max(L)

        while start + 1 < end:
            mid = (start + end) // 2

            if self.get_num_of_piece(L, mid) >= k:
                start = mid
            else:
                end = mid

        if self.get_num_of_piece(L, end) >= k:
            return end
        if self.get_num_of_piece(L, start) >= k:
            return start
        return 0

    def get_num_of_piece(self, L, length):
        piece = 0
        for l in L:
            piece = piece + l // length
        return piece

