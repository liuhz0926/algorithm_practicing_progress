class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, s, p):
        return self.is_match_with_memo(s, 0, p, 0, {})

    # source 从i开始的后缀能否匹配上pattern 从j开始的后缀
    # 能return True
    # size of pattern and source is O(n) (最多一样长）
    # 状态总数 * 每个状态的处理时间

    def is_match_with_memo(self, source, i, pattern, j, memo):

        # 查memo记录：
        if (i, j) in memo:
            return memo[(i, j)]

        # 递归的出口: 最后一位已经过了，i和j是 他们的长度
        # source 到最后一位了后面没有了
        # (这里如果其实pattern后面也没有了也没关系，因为我们all star检查的是不能出现任何一个不是star的，如果是空的也是true)
        if i == len(source):
            # check pattern is all star or not. pattern should be all star
            return self.is_all_star(pattern, j)
        # source还有剩下没return，则pattern没了，那肯定不match
        if j == len(pattern):
            return False

        # 递归的拆解，看当前pattern的j是不是star
        if pattern[j] != '*':
            match = self.is_char_match(source[i], pattern[j]) and self.is_match_with_memo(source, i + 1, pattern, j + 1,
                                                                                          memo)
        else:
            # 如果pattern是star，分成两种：star match 空，starmatch至少一个。
            match = self.is_match_with_memo(source, i, pattern, j + 1, memo) or self.is_match_with_memo(source, i + 1,
                                                                                                        pattern, j,
                                                                                                        memo)

        # memo记录：
        memo[(i, j)] = match

        return match

    def is_all_star(self, pattern, j):
        for index in range(j, len(pattern)):
            if pattern[index] != '*':
                return False
        # 都看过了都是star才能return True。如果pattern也没有其实也会直接return true
        return True

    def is_char_match(self, s_char, p_char):
        return s_char == p_char or p_char == '?'