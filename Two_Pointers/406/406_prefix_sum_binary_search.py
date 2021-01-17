class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray

    前缀和+二分答案：Time O(nlogn) Space O(n)
    """

    def minimumSize(self, nums, s):
        if not nums:
            return -1

        prefix_sum = self.get_prefix_sum(nums)

        min_size = float('inf')

        for start in range(len(nums)):
            end = self.binary_search_for_end(prefix_sum, start, s)
            print(end)
            if prefix_sum[end + 1] - prefix_sum[start] >= s:
                min_size = min(min_size, end + 1 - start)

        if min_size == float('inf'):
            return -1
        return min_size

    def binary_search_for_end(self, prefix_sum, start, s):
        # 二分答案找end
        # 因为prefix sum长度为n+1，所以right 要-2
        left, right = start, len(prefix_sum) - 2
        while left + 1 < right:
            mid = left + (right - left) // 2
            if prefix_sum[mid + 1] - prefix_sum[start] >= s:
                right = mid
            else:
                left = mid
        if prefix_sum[left + 1] - prefix_sum[start] >= s:
            return left
        return right

    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum
