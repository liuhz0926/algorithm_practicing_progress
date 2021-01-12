class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        unique_candidates = sorted(list(set(candidates)))
        results = []
        self.dfs(unique_candidates, target, 0, [], results)
        return results

    # 选了大的数字后就不能再选小的数字了。所以依然需要保留start index
    def dfs(self, unique_candidates, target, start_index, combination, results):
        if sum(combination) > target:
            return

        if sum(combination) == target:
            results.append(list(combination))
            return

        for i in range(start_index, len(unique_candidates)):
            combination.append(unique_candidates[i])
            # 因为可以重复所以还可以选当前这个数字，但是不能选前一个数字。
            # 我们必须避免先把小的都选光的case
            self.dfs(unique_candidates, target, i, combination, results)
            combination.pop()

