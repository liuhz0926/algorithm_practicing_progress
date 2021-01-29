class Solution:
    """
    @param a: an array
    @param k: the kth
    @return: return the kth subarray
    https://www.jiuzhang.com/solution/the-kth-subarray/
    难，需要数学证明
    """
    def can(self, a, x):
        n = len(a)
        # res 子数组和超过x的数量
        # n*(n+1)/2-res  子数组和不超过x的数量
        res = 0
        # 双指针开始位置，结束位置
        # 对于每个start，找到最小的end，使得[start,end]求和大于x
        # [start,end],[start,end+1],[start,end+2].....[start,n-1] 求和都会大于x
        # 这样就找到了 n-end个区间使得 子数组和大于x
        # 若start1<start2,则对应的end1<=end2
        start = 0
        end = 0
        sum = a[start]
        while start < n:
            # 不停的扩展，end，直到子数组和大于x 或者end到达边界
            while sum <= x:
                end += 1
                if (end >= n):
                    break
                sum += a[end]
            # [start,end],[start,end+1],[start,end+2].....[start,n-1] 求和都会大于x
            if end < n:
                res += n - end
            # start移动到下一个位置
            sum -= a[start]
            start += 1
        # 总的子数组数量减去大于x的子数组的数量
        return (n + 1) * n // 2 - res
    def thekthSubarray(self, a, k):
        # wrrite your code here
        n = len(a)
        left = 0
        right = 0
        for i in range(n):
            right += a[i]
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.can(a, mid) >= k:
                right = mid
            else:
                left = mid
        return right