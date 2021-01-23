class Solution:
    """
    @param s: a string
    @return: an integer

    for left写法
    """

    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        right = 0
        letter_set = set()
        max_length = 1

        for left in range(len(s)):
            # 挪right 当right的单词不在set里面
            while right < len(s) and s[right] not in letter_set:
                letter_set.add(s[right])
                right += 1
            # 记录答案
            max_length = max(max_length, right - left)
            # 挪left
            letter_set.remove(s[left])

        return max_length