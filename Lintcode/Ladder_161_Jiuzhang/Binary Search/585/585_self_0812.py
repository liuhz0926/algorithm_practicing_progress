class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        if not nums:
            return -1
        # find the last index i so that nums[i] < nums[i + 1]
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # mid + 1 保证不会越界，因为start和end是start + 1 < end
            if nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid

        # 直接看start和end谁最大return最大值(不能用二分法+1的方法判断，因为可能会越界)
        return max(nums[start], nums[end])