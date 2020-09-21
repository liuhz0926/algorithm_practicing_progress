import heapq


class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    def topk(self, nums, k):
        minheap = []

        for num in nums:
            heapq.heappush(minheap, num)
            if len(minheap) > k:
                heapq.heappop(minheap)

        return sorted(minheap, reverse=True)