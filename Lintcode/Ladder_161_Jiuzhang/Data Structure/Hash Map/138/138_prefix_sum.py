class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        # Prefix Sum 的方式：这里要记录初始0，
        # hashset记录prefix sum：index的方式
        # 这里只要是出现了一个prefixsum是前面出现过的（不一定是0，就代表这中间相当于做了一个加减然后又回到了这个sum
        # 这意味着这中间从上一个prefix sum的下一个index 到当前的index和就是0

        # 记录一下sum0和前一个index -1
        prefix_sum = 0
        prefix_sum_to_index = {prefix_sum: -1}

        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum in prefix_sum_to_index:
                return [prefix_sum_to_index[prefix_sum] + 1, i]
            prefix_sum_to_index[prefix_sum] = i

        return [-1, -1]