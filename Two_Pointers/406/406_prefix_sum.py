class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray

    前缀和：Time O(n^2) Space O(n) 超时
    """

    def minimumSize(self, nums, s):
        if not nums:
            return -1

        prefix_sum = self.get_prefix_sum(nums)

        min_size = float('inf')

        for start in range(len(nums)):
            for end in range(start, len(nums)):
                if prefix_sum[end + 1] - prefix_sum[start] >= s:
                    min_size = min(min_size, end + 1 - start)

        if min_size == float('inf'):
            return -1
        return min_size

    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum
