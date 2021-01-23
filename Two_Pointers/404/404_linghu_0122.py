class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """

    def subarraySumII(self, A, start, end):
        if not A:
            return 0
        # 不用sort！只是找区间和在那里面的
        n = len(A)

        smaller_sum, bigger_sum = 0, 0
        right_start, right_end = 0, 0
        result = 0

        for left in range(n):
            # left 移动后，如果right 在left前面，因为我们可能left一个数字也是在范围内，
            # 但是如果right就在右边，那还是不动
            # 这里用max来解决
            right_start = max(right_start, left)
            right_end = max(right_end, left)

            # 下限，没到start一直挪right，到了开始挪left
            while right_start < n and smaller_sum + A[right_start] < start:
                smaller_sum += A[right_start]
                right_start += 1

            # 上限，超了end才不加了，开始挪left
            while right_end < n and bigger_sum + A[right_end] <= end:
                bigger_sum += A[right_end]
                right_end += 1

            # if right_end - right_start > 0: (令狐答案有这句，但是这样避免了+0的情况，rightend不会超过rightstart)
            result += right_end - right_start

            # 开始挪left
            # 必须确保right 都在left前面才能，如果他们合并在一起，比如start end都是0，那就不该做-left，这样sum会变成负的
            if right_start > left:
                smaller_sum -= A[left]
            if right_end > left:
                bigger_sum -= A[left]

        return result
