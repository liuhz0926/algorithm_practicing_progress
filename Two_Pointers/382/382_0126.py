class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        if len(S) < 3:
            return 0

        S.sort()

        count = 0
        # 从第三个开始循环c
        for c in range(2, len(S)):
            left, right = 0, c - 1

            while left < right:
                if S[left] + S[right] > S[c]:

                    # 注意这里！这两个的和没问题的话left左边所有left都可以和right
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count
