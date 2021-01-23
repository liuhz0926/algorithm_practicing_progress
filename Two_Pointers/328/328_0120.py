class Solution:
    """
    @param s: a string
    @return:  an array containing the length of each part
    """

    def splitString(self, s):
        if not s:
            return []

        # 算出每一个字幕的last position
        last_pos = {}
        for i in range(len(s)):
            last_pos[s[i]] = i

        result = []
        left = 0

        # right寻找每一个left和right之间的字母的last position
        # 直到二者相遇
        while left < len(s):
            # start记录最开始left的位置，然后right记录最开始的last position
            start = left
            right = last_pos[s[left]]

            # 开始移动left直到两者相遇，期间right一直根据两者中间的单词挪动last position
            while right < len(s) and left < right:
                right = max(right, last_pos[s[left]])
                left += 1

            # 两者相遇说明这段结束，记录从start 到最后这个right的last position的位置，
            # 新的left 下一段从目前right的下一个开始
            result.append(right - start + 1)
            left = right + 1

        return result