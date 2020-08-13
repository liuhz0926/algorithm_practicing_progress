class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        if not nums:
            return None

        # 通过我们知道左半部分一定比右半部分大来区分start和end
        # 另外找的是右边的first element。所以主要看mid和当前end的大小区别
        # 要是求最大值就是求左半部分的last，就是mid要跟start比
        # 最后剩下两个。只要start和end的最小值
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

        return min(nums[start], nums[end])