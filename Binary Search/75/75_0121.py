class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        if not A:
            return None

        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid - 1] < A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid

        if A[start] > A[end]:
            return start
        return end