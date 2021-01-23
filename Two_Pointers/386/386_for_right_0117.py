class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s or not k:
            return 0

        left = 0
        letter_to_count = {}
        max_length = 0

        # 最多k个超过k个要减少挪left
        for right in range(len(s)):
            letter_to_count[s[right]] = letter_to_count.get(s[right], 0) + 1

            # 最多k个，多了移动left
            while left <= right and len(letter_to_count) > k:
                letter_to_count[s[left]] -= 1
                if letter_to_count[s[left]] == 0:
                    del letter_to_count[s[left]]
                left += 1

            # 不到k个记录
            max_length = max(max_length, right + 1 - left)

        return max_length