class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        # write your code here
        if not A:
            return -1

        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            # 全增加形式，替换start
            if A[mid - 1] < A[mid] < A[mid + 1]:
                start = mid
            # 全降低形式，替换end
            elif A[mid - 1] > A[mid] > A[mid + 1]:
                end = mid
            # peak的情况
            elif A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
            else:
                # local min
                # either start or end is ok
                end = mid

        return -1