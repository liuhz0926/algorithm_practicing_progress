class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        if not nums:
            return [[]]

        sorted_nums = sorted(nums)
        all_permutations = []
        # Here we write down the index of nums not num itself since there are multiple
        visited_index = set()
        self.dfs(sorted_nums, [], visited_index, all_permutations)
        return all_permutations

    # 1 递归的定义：找到所有permutation开头的排列，加到results（all_permutations）里面
    def dfs(self, sorted_nums, permutation, visited_index, all_permutations):
        # 2 递归的出口
        if len(permutation) == len(sorted_nums):
            all_permutations.append(list(permutation))

        # 3 递归的拆解
        for i in range(len(sorted_nums)):
            if i in visited_index:
                continue
            # 当前的数和前面一样，确保大于0，否则index无效.
            # 而且！前面这个数字必须没用过，我们要12’2“，但是不要12"2'，注意这里12”的时候其实就应该砍掉了，因为2‘没有用
            if i > 0 and sorted_nums[i - 1] == sorted_nums[i] and (i - 1) not in visited_index:
                continue
            permutation.append(sorted_nums[i])
            visited_index.add(i)
            self.dfs(sorted_nums, permutation, visited_index, all_permutations)
            permutation.pop()
            visited_index.remove(i)

