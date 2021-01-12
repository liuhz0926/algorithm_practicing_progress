class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # 和subsets那道题很类似（combination）
        if not nums:
            return [[]]

        all_permutations = []
        visited = set()
        self.dfs(nums, [], visited, all_permutations)
        return all_permutations

    # 递归的定义：找到所有的permutation开头的permutations
    def dfs(self, nums, permutation, visited, all_permutations):
        # 递归的出口
        if len(permutation) == len(nums):
            all_permutations.append(list(permutation))

        # 递归的拆解：
        # [] -> [1] [2] [3]
        # [1] -> [12] [13]
        # [12] -> [123]
        for num in nums:
            if num in visited:
                continue
            # not in visited
            permutation.append(num)
            visited.add(num)
            self.dfs(nums, permutation, visited, all_permutations)
            # backtracking
            permutation.pop()
            visited.remove(num)