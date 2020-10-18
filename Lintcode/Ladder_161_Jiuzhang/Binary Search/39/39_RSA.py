class Solution:
    """
    无重复
    @param nums: An integer array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if not nums:
            return []

        # take O(logn)
        # 因为有重复，只能打擂台找最小
        # 只要找到gap。前面那位比这一位大就是minIndex
        for index in range(len(nums)):
            if nums[index] < nums[index - 1]:
                minIndex = index
                break
        # 把左半部分交换变成降序
        # 把右半部分交换变成降序 这样就连接上了
        # 然后从头到尾交换
        # 时间2O（n）
        self.rotateArray(nums, 0, minIndex - 1)
        self.rotateArray(nums, minIndex, len(nums) - 1)
        self.rotateArray(nums, 0, len(nums) - 1)

    def rotateArray(self, nums, left, right):
        # 左右交换颠倒
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if not nums:
            return []

        # take O(logn)
        minIndex = self.find_min(nums)
        # 把左半部分交换变成降序
        # 把右半部分交换变成降序 这样就连接上了
        # 然后从头到尾交换
        # 时间2O（n）
        self.rotateArray(nums, 0, minIndex - 1)
        self.rotateArray(nums, minIndex, len(nums) - 1)
        self.rotateArray(nums, 0, len(nums) - 1)

    def find_min(self, nums):
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

        if nums[start] < nums[end]:
            return start
        else:
            return end

    def rotateArray(self, nums, left, right):
        # 左右交换颠倒
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1