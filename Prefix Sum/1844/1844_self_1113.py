class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """

    def subarraySumEqualsKII(self, nums, k):
        """
        整体思想：subarray的和其实就可以想到他其实是prefixSum(end + 1) - prefixSum(start) = k
        所以循环每个end。并记录每一个prefixSum。然后同时去寻找prefixSum(end + 1) - k的start在哪里。
        如果这个出现在Sum2Index的map里面了，我们找到这个prefixSum所对应的start key。我们要的是
        从start 到 end这个长度。所以其实是end + 1 - start （因为要算start进去）
        然后把这个index去和answer 打擂台

        """
        prefixSum = self.get_prefixSum(nums)
        answer = float('inf')
        # 记录prefixSum和他的最小index。
        # 所以这里base case同时也要记录prefix sum为0的情况。
        # 因为有可能找到的是prefixsum - k为0的情况。这样就对应了其实就是找一个prefixsum就是k的情况
        # 这也是为什么，所有的end都要+1，因为end传入的是当前index。
        # 所以我们也要把basecase记录进去
        prefixSum2Idx = {0: 0}
        for end in range(len(nums)):
            if prefixSum[end + 1] - k in prefixSum2Idx:
                length = end + 1 - prefixSum2Idx[prefixSum[end + 1] - k]
                answer = min(answer, length)
            prefixSum2Idx[prefixSum[end + 1]] = end + 1
        return answer

    def get_prefixSum(self, nums):
        # 前i个数和，所以说如果是前3个数字，index在i = 3上，但是其实加的是0，1，2
        # 所以prefixsumindex为i+1。
        # 而且存在前0个数和，所以要存0
        prefixSum = [0]
        for i in range(len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])
        return prefixSum