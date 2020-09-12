class Solution:
    """
    @param str: A string
    @return: all permutations
    """

    def stringPermutation2(self, str):
        sorted_str = sorted(list(str))
        all_permutations = []
        self.dfs(sorted_str, set(), [], all_permutations)
        return all_permutations

    def dfs(self, sorted_str, visited_index, permutation, all_permutations):
        if len(permutation) == len(sorted_str):
            all_permutations.append(''.join(permutation))
            return

        for i in range(len(sorted_str)):
            if i in visited_index:
                continue
            if i > 0 and sorted_str[i - 1] == sorted_str[i] and (i - 1) not in visited_index:
                continue
            permutation.append(sorted_str[i])
            visited_index.add(i)
            self.dfs(sorted_str, visited_index, permutation, all_permutations)
            permutation.pop()
            visited_index.remove(i)

