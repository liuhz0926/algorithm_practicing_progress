class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        sorted_nums = sorted(nums)
        unique_combinations = []
        self.dfs(sorted_nums, 0, [], unique_combinations)
        return unique_combinations

    def dfs(self, sorted_nums, start_index, combination, unique_combinations):
        unique_combinations.append(list(combination))
        for i in range(start_index, len(sorted_nums)):

            # 唯一的区别，去重：start index可能和下一位是一个单词。
            # 比如122. 插入第一个2 是start index，下一个2的时候才要检查前面
            # 虽然我们必须保证i是不等于0的，，但因为>start index 一定不等于0 （所以不用写。ppt上写了，但是答案没写）
            if i > start_index and sorted_nums[i - 1] == sorted_nums[i]:
                continue

            combination.append(sorted_nums[i])
            self.dfs(sorted_nums, i + 1, combination, unique_combinations)
            combination.pop()