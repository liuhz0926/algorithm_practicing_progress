class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        if not nums:
            return 0

        # Extra Space with On Time
        i = 0
        unique = set()

        for j in range(len(nums)):
            if nums[j] in unique:
                continue
            unique.add(nums[j])
            nums[i] = nums[j]
            i += 1

        # return unique 长度，就是i
        return i


class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        if not nums:
            return 0

        # Onlogn Time
        nums.sort()

        i = 1

        for j in range(1, len(nums)):
            if nums[j - 1] == nums[j]:
                continue
            nums[i] = nums[j]
            i += 1

        # return unique 长度，就是i
        return i