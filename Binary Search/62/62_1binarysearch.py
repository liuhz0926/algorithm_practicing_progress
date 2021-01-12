class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        if not A:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # 要点：每次取一个mid的位置，都会切除一个连续的array，一个rsa
            # 所以要看target实在连续的array里面。还是在rsa里面
            # mid比start大，证明切出来左边是array，右边是rsa
            if A[mid] >= A[start]: # 和> A[end]一样，分清在那部分即可
                # 看target的位置
                # target在左边连续的array里面。那end直接放到mid来。继续正常二分法（其实就是做mid和target的对比）
                if A[start] <= target <= A[mid]:
                    end = mid
                # target在右边的rsa里面。那就左半部分抛起。从新的rsa里面拆新的
                else:
                    start = mid
            # 相反，切出来右边是array，左边是rsa
            else:
                # target在右边的array里，那start等于当前的mid进行二分
                if A[mid] <= target <= A[end]:
                    start = mid
                # target在左边的rsa里面，那就抛弃右半部分，从系的rsa里切
                else:
                    end = mid

        # 和普通的binary search一样
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1