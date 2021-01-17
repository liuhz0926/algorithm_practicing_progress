class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """

    def kDistinctCharacters(self, s, k):
        if not s:
            return 0

        char_to_count = {}
        left = 0
        num_substring = 0

        for right in range(len(s)):
            char_to_count[s[right]] = char_to_count.get(s[right], 0) + 1

            while left <= right and len(char_to_count) >= k:
                num_substring += len(s) - right

                # 挪left
                char_to_count[s[left]] -= 1
                if char_to_count[s[left]] == 0:
                    # 0了删除该点
                    del char_to_count[s[left]]
                left += 1

        return num_substring