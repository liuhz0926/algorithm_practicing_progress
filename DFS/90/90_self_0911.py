class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """

    def kSumII(self, A, k, target):
        sorted_num = sorted(A)
        results = []
        self.dfs(sorted_num, k, target, 0, [], results)
        return results

    def dfs(self, sorted_num, k, target, start_index, combination, results):
        if len(combination) > k:
            return

        if sum(combination) > target:
            return

        if sum(combination) == target and len(combination) == k:
            results.append(list(combination))
            return

        for i in range(start_index, len(sorted_num)):
            combination.append(sorted_num[i])
            self.dfs(sorted_num, k, target, i + 1, combination, results)
            combination.pop()

        return


class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """

    def kSumII(self, A, k, target):
        sorted_num = sorted(A)
        results = []
        self.dfs(sorted_num, k, target, 0, [], results)
        return results

    def dfs(self, sorted_num, k, target, start_index, combination, results):
        if target == 0 and k == 0:
            results.append(list(combination))
            return

        # 因为上一条不符合才可以这么写
        if k < 0 or target <= 0:
            return

        for i in range(start_index, len(sorted_num)):
            combination.append(sorted_num[i])
            self.dfs(sorted_num, k - 1, target - sorted_num[i], i + 1, combination, results)
            combination.pop()

        return