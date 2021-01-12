# 最优解法，minheap，add加入后，如果超出k个了，就把最小的给pop了，因为他肯定不会在top k largest里面
# 所以这里确实是用的minheap，然后我们pop的是不要的最小的
# add(logk) topk O(klogk)
import heapq

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.minheap = []
        self.k = k
    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        heapq.heappush(self.minheap, num)
        if len(self.minheap) > self.k:
            # pop 最小的因为他不在top k里面
            heapq.heappop(self.minheap)
    """
    @return: Top k element
    """
    def topk(self):
        # 只要return一个sorted minheap就可以了
        return sorted(self.minheap, reverse = True)
