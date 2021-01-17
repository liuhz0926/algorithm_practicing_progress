class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray

    同向双指针 O(n) O(1)
    """

    def minimumSize(self, nums, s):
        if not nums:
            return -1

        j = 0
        curt_sum = 0
        min_size = float('inf')

        # 同向双指针模板：L因为要走到头所以用for loop
        for i in range(len(nums)):
            # R 在sum小于的时候一直往后推，推到大了停止
            while curt_sum < s and j < len(nums):
                curt_sum += nums[j]
                j += 1
            # 这里要加if因为如果改变L的时候也要check sum的大小
            if curt_sum >= s:
                # 打擂台记录
                min_size = min(min_size, j - i)
            # 移动L之前吧这段在sum里面扣除
            curt_sum -= nums[i]

        if min_size == float('inf'):
            return -1
        return min_size
