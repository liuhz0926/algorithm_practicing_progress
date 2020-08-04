class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        # write your code here
        if not nums:
            return 0

        count = 0
        sorted_nums = sorted(nums)

        left, right = 0, len(sorted_nums) - 1
        last_pair = (0, 0)
        while left < right:
            if sorted_nums[left] + sorted_nums[right] < target:
                left += 1
            elif sorted_nums[left] + sorted_nums[right] > target:
                right -= 1
            else:
                if last_pair != (sorted_nums[left], sorted_nums[right]):
                    count += 1
                    last_pair = (sorted_nums[left], sorted_nums[right])
                left, right = left + 1, right - 1

        return count