class Solution:
    """
    @param source: A string
    @param words: A list of string
    @return: return list of words[i] that is a subsequence of source.
    """

    def MatchingSubsequences(self, source, words):
        if not source or not words:
            return []

        result = []
        for word in words:
            # 每一个单词同向双指针
            if self.is_macth_word(source, word):
                result.append(word)

        return result

    def is_macth_word(self, source, word):
        # 同向双指针
        j = 0
        for i in range(len(source)):
            if j < len(word) and source[i] == word[j]:
                j += 1

        if j == len(word):
            return True
        return False
