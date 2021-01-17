class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray

    while写法，先移动right再移动left
    """

    def minimumSize(self, nums, s):
        if not nums:
            return -1

        left, right = 0, 0
        curt_sum = 0
        min_size = float('inf')

        while left < len(nums) and right < len(nums):

            while right < len(nums) and curt_sum < s:
                curt_sum += nums[right]
                right += 1

            while left <= right and curt_sum >= s:
                # 刚好相等了 right多走了一位，right前一位到left的长度
                min_size = min(min_size, right - left)
                curt_sum -= nums[left]
                left += 1

        if min_size == float('inf'):
            return -1
        return min_size