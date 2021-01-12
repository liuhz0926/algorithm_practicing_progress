class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):
        # 两次partition
        # 第一次拍0组 和12组
        left_0 = self.twopartition(nums, 0, 0)
        # 第二次排1和2组
        self.twopartition(nums, 1, left_0)

        return nums

    def twopartition(self, nums, color, start):
        # 普通partition我们是partition从0到最后。这里因为要partition两次。
        # 所以第一次是从0到最后。因为只分一个class
        # 第二次分两个class。就是从当时第一组的最后一个left 的位置。为后面两个color的分组起始点
        left, right = start, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] == color:
                left += 1
            while left <= right and nums[right] != color:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return left
