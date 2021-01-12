class Solution:
    """
    求方案总数
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        max_length, lower_dict = self.get_maxlength_lowercase(dict)
        return self.dfs_memo(s.lower(), 0, lower_dict, max_length, {})

    def dfs_memo(self, s, index, dict, max_length, memo):
        if index in memo:
            return memo[index]

        # 递归出口，只有一种方案，注意不是0种方案
        if index == len(s):
            return 1

        # 找到一种 + 1
        memo[index] = 0
        for i in range(index, len(s)):
            # 超限额
            if i + 1 - index > max_length:
                break

            prefix = s[index: i + 1]
            if prefix not in dict:
                continue
            # 在字典里, 这个点的方案总和等于下面所有子问题的方案总和
            # 比如 lintcode分lint的3index的方案等于 code分成 code和co de两种的方案总和
            memo[index] += self.dfs_memo(s, i + 1, dict, max_length, memo)
        # 注意要return memo否则没法检查
        return memo[index]

    # 因为可以忽略case所以我们也统一lower了
    def get_maxlength_lowercase(self, dict):
        max_length = 0
        lower_dict = set()
        for word in dict:
            max_length = max(max_length, len(word))
            lower_dict.add(word.lower())
        return max_length, lower_dict