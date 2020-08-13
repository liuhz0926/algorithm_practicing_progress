class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):

        # Step 1 look for where is the boundary of the number upper(right) and lower(left)
        right = self.findUpperCloeset(A, target)
        left = right - 1

        # Step 2 find the closest numbers in number of k, so we have a for loop in k
        result = []
        for _ in range(k):
            # we need to judge right left which one is smaller
            if self.isLeftCloesr(A, target, left, right):
                result.append(A[left])
                # 有点像反向双指针，left right反向走
                left -= 1
            else:
                result.append(A[right])
                right += 1

        return result

    def findUpperCloeset(self, A, target):
        # find the first right number which is >= the target using Binary search
        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            # 一旦大于先把end无线往小了改。直到数组只有一个start 一个end，那必定有一个数字是right upper closest
            if A[mid] >= target:
                end = mid
            else:
                start = mid

        # 优先看start
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end

        # 找不到right的情况。说明所有的数字都要小，lower closest就是最后一个数字。所以当前的right是len(A)
        return len(A)

    def isLeftCloesr(self, A, target, left, right):
        # left 非零， right大于长度。则一定只剩下另一种
        if left < 0:
            return False
        if right >= len(A):
            return True
        # 其他情况return这个比大小的statement
        return target - A[left] <= A[right] - target
