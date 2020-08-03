class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        if not numbers:
            return [-1, -1]

        nums = sorted([(val, index) for index, val in enumerate(numbers)])

        left, right = 0, len(nums) - 1
        while left < right:
            sum = nums[left][0] + nums[right][0]
            if sum == target:
                return sorted([nums[left][1], nums[right][1]])
            elif sum > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]