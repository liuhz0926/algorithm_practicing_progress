class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, dict())

    def dfs(self, s, wordDict, memo):
        # 算过了
        if s in memo:
            return memo[s]

        # 算完了，空串了，递归出口
        if len(s) == 0:
            return []

        partitions = []

        # 取prefix，所以i从1开始
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            # 在worddict里面, we will get the rest partition from recursively
            rest_partition = self.dfs(s[i:], wordDict, memo)
            # we need to combine them together for each of them with the prefix,
            # forinstance: current prefix: lint, other rest: code and co de
            # so we need to combine them into lint code and lint co de
            for subpart in rest_partition:
                partitions.append(prefix + ' ' + subpart)

        # remeber to add if the whole word is in Dict, 这个有必要要加，因为如果整个单词都在里面，则rest partition返回[]，所以就没有加进去subpart
        if s in wordDict:
            partitions.append(s)

        # 记录partition 比如alintcode，a和后面两个分支其实都不用再扫不同的了
        memo[s] = partitions
        return partitions