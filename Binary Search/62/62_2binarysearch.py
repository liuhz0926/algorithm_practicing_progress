class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        if not A:
            return -1
        # 方法一 两次二分
        # 先找min的位置
        min = self.findMin(A)

        if A[min] <= target <= A[-1]:
            return self.binarySearch(A, min, len(A) - 1, target)
        else:
            return self.binarySearch(A, 0, min - 1, target)

    def findMin(self, A):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[end]:
                start = mid
            else:
                end = mid
        if A[start] < A[end]:
            return start
        else:
            return end

    def binarySearch(self, A, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
