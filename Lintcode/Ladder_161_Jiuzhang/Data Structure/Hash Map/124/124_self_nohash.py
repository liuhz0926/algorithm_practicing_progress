class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, num):
        num_set = set(num)
        max_len = 0

        for num in num_set:
            # we can start from this by adding one
            if num - 1 in num_set:
                continue

            count = 0
            # until we find the last one don't have next
            while num in num_set:
                count += 1
                num += 1

            max_len = max(max_len, count)

        return max_len

