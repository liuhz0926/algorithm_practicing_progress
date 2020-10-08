class Solution:
    """
    192 Followup

    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
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
            # pattern 必须是空的，或者其他的字母后面都有*（代表0）
            return self.is_empty(pattern[j:])
        # source还有剩下没return，则pattern没了，那肯定不match
        if j == len(pattern):
            return False

        # 递归的拆解，pattern当前下一位是star，(要确保不能过界，index 所以先判断下j + 1的长度)
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            # pattern 这个j位使用多次或者零次(注意零次是+2)
            match = (self.is_char_match(source[i], pattern[j]) and self.is_match_with_memo(source, i + 1, pattern, j,
                                                                                           memo)) or self.is_match_with_memo(
                source, i, pattern, j + 2, memo)
        else:
            # 下一位不是star 直接compare 当前位置
            match = self.is_char_match(source[i], pattern[j]) and self.is_match_with_memo(source, i + 1, pattern, j + 1,
                                                                                          memo)

        # memo记录：
        memo[(i, j)] = match

        return match

    def is_empty(self, pattern):
        # 必须是偶数个：0 或者每一个字母带*
        if len(pattern) % 2 != 0:
            return False

        # check 每一个后面都有star，在奇数位上。1 3 5
        for i in range(len(pattern) // 2):
            if pattern[i * 2 + 1] != '*':
                return False
        return True

    def is_char_match(self, s_char, p_char):
        return s_char == p_char or p_char == '.'
