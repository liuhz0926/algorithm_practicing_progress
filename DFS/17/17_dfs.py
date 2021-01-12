class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        # 就算nums 是空，也应该return空所以不用单独写了
        sorted_nums = sorted(nums)
        all_combinations = []
        self.dfs(sorted_nums, 0, [], all_combinations)
        return all_combinations

    def dfs(self, sorted_nums, index, combination, all_combinations):
        # 注意这里需要make a new copy of combination，否则在回溯的过程中，其实是copy的一个地址，因为不断地修改这个combination
        # 可以用list(combination)来做copy
        all_combinations.append(combination.copy())

        for i in range(index, len(sorted_nums)):
            combination.append(sorted_nums[i])
            # 导入的index其实就是下一位，而不是当前combination的最后一位
            self.dfs(sorted_nums, i + 1, combination, all_combinations)
            # 回溯
            combination.pop()