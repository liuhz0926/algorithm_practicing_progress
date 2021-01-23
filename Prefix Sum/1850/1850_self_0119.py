class Solution:
    """
    @param A: a list of integer
    @param K: a integer
    @param L: a integer
    @return: return the maximum number of apples that they can collect.
    """

    def PickApples(self, A, K, L):
        if K + L > len(A):
            return -1

        prefix_sum = self.get_prefix_sum(A)

        result = -1

        # 左边是K 右边是 L (左边要保留k，L可以从index K 开始，右边最远到n-L，因为要剩下L个)
        max_k = 0
        for i in range(K, len(prefix_sum) - L):
            max_k = max(max_k, prefix_sum[i] - prefix_sum[i - K])
            # 加上后半段
            result = max(result, max_k + (prefix_sum[i + L] - prefix_sum[i]))

        # 左边是L 右边是K (反过来)
        max_l = 0
        for i in range(L, len(prefix_sum) - K):
            max_l = max(max_l, prefix_sum[i] - prefix_sum[i - L])
            # 加上后半段
            result = max(result, max_l + (prefix_sum[i + K] - prefix_sum[i]))

        return result

    def get_prefix_sum(self, A):
        prefix_sum = [0]
        for i in range(len(A)):
            prefix_sum.append(prefix_sum[-1] + A[i])
        return prefix_sum