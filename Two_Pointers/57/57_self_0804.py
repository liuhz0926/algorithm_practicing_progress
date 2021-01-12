class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here
        if not numbers:
            return []

        sorted_nums = sorted(numbers)
        result = []

        # 细节优化， 这里i最多到length - 2，因为后面有两个数字
        for i in range(len(sorted_nums)):
            # 并且可以直接跳过i前后的值相同的情况。因为找出来的结果会是雷同的
            # if i > 0 and nums[i] == nums[i - 1]:
            # continue
            left, right = i + 1, len(sorted_nums) - 1
            self.find_two_sum(left, right, sorted_nums, -sorted_nums[i], result)

        return result

    def find_two_sum(self, left, right, sorted_nums, target, result):
        while left < right:
            if sorted_nums[left] + sorted_nums[right] < target:
                left += 1
            elif sorted_nums[left] + sorted_nums[right] > target:
                right -= 1
            else:
                triplet = sorted([sorted_nums[left], sorted_nums[right], -target])
                # 查去重
                if triplet not in result:
                    result.append(triplet)
                left += 1
                right -= 1
                # 因为会存在left right 挪了一位后 还是同一组数字，所以另外一个去重的方法是
                # 这个必须结合上面if nums[i] == nums[i-1]的方法
                # while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                # left += 1
                # while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                # right -= 1