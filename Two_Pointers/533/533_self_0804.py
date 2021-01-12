class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """

    def twoSumClosest(self, nums, target):
        # write your code here
        if not nums:
            return None

        sorted_nums = sorted(nums)
        # set min_sum is none
        min_sum = None
        left, right = 0, len(sorted_nums) - 1

        while left < right:
            # check if the sum is the min
            two_sum = sorted_nums[left] + sorted_nums[right]

            # Have to use is None 而不是not min_sum
            # not min_sum 当min_sum为0的时候也是true。所以这里必须是is None的判定
            if min_sum is None or abs(two_sum - target) < abs(min_sum - target):
                min_sum = two_sum

            # sum is larger or less, move left, right
            if two_sum <= target:
                left += 1
            else:
                right -= 1

        return abs(min_sum - target)