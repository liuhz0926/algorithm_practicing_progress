"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

import heapq


# min heap 的class, pop的是最小的，我们这里要保留k个最小的，所以用-distance来表示，同样-x -y

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        heap = []

        for point in points:
            dist = self.get_distance(point, origin)
            # 必须把x y写出来来而不是直接写point，因为same distance要根据x排序，然后根据y
            heapq.heappush(heap, (-dist, -point.x, -point.y))

            if len(heap) > k:
                # 把最小的-dist 抛出，其实是最大的
                heapq.heappop(heap)

        result = []
        while heap:
            _, x, y = heapq.heappop(heap)
            # 加入的是最远的我们最后要reverse一下
            result.append(Point(-x, -y))

        result.reverse()
        return result

    def get_distance(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2