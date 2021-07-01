class Solution:
    """
    # 这份代码会stack overflow 因为时间为O（nL)
    L 是wordset长，n是input string长，如果n很长递归深度是n，容易Stack Overflow


    @param s: A string
    @param wordSet: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, wordSet):
        max_length = self.get_max_length(wordSet)
        return self.is_possible(s, 0, max_length, wordSet, {})

    def is_possible(self, s, index, max_length, wordSet, memo):
        # 在memo里面返回
        if index in memo:
            return memo[index]

        # 递归出口，到最后一位了，空字串
        if index == len(s):
            return True

        memo[index] = False
        for i in range(index, len(s)):
            # 超过长度，说明没有这个单词
            if i + 1 - index > max_length:
                break
            prefix = s[index: i + 1]
            # 没有这个单词, 下一个prefix
            if prefix not in wordSet:
                continue
            # 有这个单词的话, 前缀划分了，下一个单词从当前的后缀开始，如果也能划分说明现在这个划分是对的。
            # 因为可以划分为helloween 和hello两种必须后面也成功前面这个才能ok
            if self.is_possible(s, i + 1, max_length, wordSet, memo):
                # 当前划分了，且下一位也ok
                memo[index] = True
                break
        return memo[index]

    def get_max_length(self, wordSet):
        # 打擂台寻找最大的word长度
        max_length = 0
        for word in wordSet:
            max_length = max(max_length, len(word))
        return max_length