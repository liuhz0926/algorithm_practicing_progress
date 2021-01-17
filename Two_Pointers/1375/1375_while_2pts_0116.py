class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """

    def kDistinctCharacters(self, s, k):
        if not s:
            return 0

        left, right = 0, 0
        char_to_count = {}
        num_substring = 0

        while left < len(s) and right < len(s):

            while right < len(s) and len(char_to_count) < k:
                char_to_count[s[right]] = char_to_count.get(s[right], 0) + 1
                right += 1

            # 出了后right 是在下一位后加了1
            while left <= right and len(char_to_count) >= k:
                num_substring += len(s) - right + 1
                char_to_count[s[left]] -= 1
                if char_to_count[s[left]] == 0:
                    del char_to_count[s[left]]
                left += 1

        return num_substring