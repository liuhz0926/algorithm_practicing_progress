import heapq


class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """

    def nthUglyNumber(self, n):
        # 用heap每次把最小的拿出来，x2， x3， x5， 然后加进去，因为heap一定保证pop出来的是最小的，所以是按照顺序的
        # 记录第几个visited过的
        heap = [1]
        visited = set([1])
        # pop 第n词的时候，就是第n个, 以防万一先写上none
        value = None
        for i in range(n):
            value = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if value * factor not in visited:
                    visited.add(value * factor)
                    # heappush因为要siftup所以是logn时间
                    heapq.heappush(heap, value * factor)

        return value