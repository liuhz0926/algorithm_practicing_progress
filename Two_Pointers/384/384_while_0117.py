class Solution:
    """
    @param s: a string
    @return: an integer

    while写法
    """

    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        left, right = 0, 0
        letter_set = set()
        max_length = 0

        while left < len(s) and right < len(s):

            # 挪right: 直到遇到第一个重复的
            while right < len(s) and s[right] not in letter_set:
                letter_set.add(s[right])
                right += 1

            # 刚好第一个重复的了，right在第一个重复的位置里面
            while left < right and (right == len(s) or s[right] in letter_set):
                # 记录答案
                max_length = max(max_length, right - left)

                # 挪left
                letter_set.remove(s[left])
                left += 1

        return max_length