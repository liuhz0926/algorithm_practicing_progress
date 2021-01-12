class Solution:
    """
    @param nums: the array of integers
    @param target:
    @return: the starting and ending position
    """

    def searchRange(self, nums, target):
        n = len(nums)
        return [self.searchFirst(nums, 0, n - 1, target), self.searchLast(nums, 0, n - 1, target)]

    def searchFirst(self, nums, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def searchLast(self, nums, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1