class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """

    def twoSum2(self, nums, target):
        # write your code here
        if not nums:
            return 0

        sorted_nums = sorted(nums)
        count = 0
        left, right = 0, len(sorted_nums) - 1

        while left < right:
            if sorted_nums[left] + sorted_nums[right] > target:
                count += right - left
                right -= 1
            else:
                left += 1

        return count
