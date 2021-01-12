class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        # 找的是升序排列中的第k-1个
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)

    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(left + right) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # 第k位比当前的right小。说明是在左半部分里面
        if k <= right:
            return self.quickSelect(nums, start, right, k)
        # 第k位比当前left 大，说明是在右半部分里面。
        # 我们找的都是index位k的
        elif k >= left:
            return self.quickSelect(nums, left, end, k)

        return nums[k]