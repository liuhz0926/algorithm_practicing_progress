# 用quick select的话。就是select kth largest element 通过partition 二分法的方式时间是O(n)
# 然后一个一个循环去找比他大的，加入到list里面，然后再sort（用klogk时间）
# add O(1) topk O(n+klogk)
# maxheap的方法，和612方法一样，但是不是最优解法，因为pop min后还要push回去
# 而且其实需要记录最大的k个就可以了而不是所有都记录
# add(logn) topk O(nlogk)
import heapq


class Solution:
    """
    @param: k: An integer
    """

    def __init__(self, k):
        self.maxheap = []
        self.k = k

    """
    @param: num: Number to be added
    @return: nothing
    """

    def add(self, num):
        heapq.heappush(self.maxheap, -num)

    """
    @return: Top k element
    """

    def topk(self):
        top_k = []
        for _ in range(self.k):
            if not self.maxheap:
                break
            top_k.append(-heapq.heappop(self.maxheap))
        for num in top_k:
            heapq.heappush(self.maxheap, -num)

        return top_k

