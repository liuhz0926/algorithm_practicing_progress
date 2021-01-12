class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """

    def wordPatternMatch(self, pattern, str):
        return self.is_match(pattern, str, dict(), set())

    def is_match(self, pattern, string, mapping, used):
        # dfs 递归出口
        if not pattern:
            # string空了才是true
            return not string

        pattern_letter = pattern[0]
        if pattern_letter in mapping:
            word = mapping[pattern_letter]
            # 查看现在的string是不是以这个word开始的
            if not string.startswith(word):
                return False
            # 去看下一阶段，从这个单词后面开始
            return self.is_match(pattern[1:], string[len(word):], mapping, used)

        for i in range(len(string)):
            word = string[: i + 1]
            # 前面一个pattern letter已经用了这个单词了
            if word in used:
                continue
            used.add(word)
            mapping[pattern_letter] = word
            if self.is_match(pattern[1:], string[i + 1:], mapping, used):
                return True
            # backtracking
            del mapping[pattern_letter]
            used.remove(word)

        # 都不行
        return False


