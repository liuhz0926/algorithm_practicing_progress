import heapq
# 使用 Heapq 的方法 最快，因为不需要创建额外空间。 时间复杂度和其他的算法一致，都是 O(nlogk) 是所有元素个数

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        heap = []
        for index, array in enumerate(arrays):
            if not array:
                continue
            heapq.heappush(heap, (array[0], index, 0))

        result = []
        while heap:
            num, array_index, num_index = heapq.heappop(heap)
            result.append(num)
            if num_index + 1 < len(arrays[array_index]):
                heapq.heappush(heap, (arrays[array_index][num_index + 1], array_index, num_index + 1))

        return result