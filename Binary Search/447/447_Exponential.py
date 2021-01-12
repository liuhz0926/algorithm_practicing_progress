class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """

    def searchBigSortedArray(self, reader, target):
        if not reader:
            return -1

        # try to find a big number that is bigger than the target
        # Exponential Backoff 倍增法, 从第一位index 0开始所以kth - 1
        kth = 1
        while reader.get(kth - 1) < target:
            kth = kth * 2

        # 二分法基础模板
        start, end = 0, kth - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end

        return -1