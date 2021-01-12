class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        return self.quick_sort(nums, 0, len(nums) - 1, len(nums) - n)

    def quick_sort(self, nums, start, end, k):

        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1


        if k >= left:
            self.quick_sort(nums, left, end, k)
        if k <= right:
            self.quick_sort(nums, start, right, k)

        # 递归出口
        return nums[k]