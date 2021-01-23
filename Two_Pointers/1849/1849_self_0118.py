class Solution:
    """
    @param customers: the number of customers
    @param grumpy: the owner's temper every day
    @param X: X days
    @return: calc the max satisfied customers
    """

    def maxSatisfied(self, customers, grumpy, X):

        curt_sum = 0
        # Case 0 to X-1 的sum过了X-1有1就跳过
        for i in range(len(customers)):
            if i >= X and grumpy[i] == 1:
                continue
            curt_sum += customers[i]

        left = 0
        max_sum = 0
        for right in range(X - 1, len(customers)):

            # 除了最开始X-1的位置，下一个位置每一次right都要如果是1都要加上
            if right != X - 1 and grumpy[right] == 1:
                curt_sum += customers[right]

            # 记录比较答案
            max_sum = max(max_sum, curt_sum)

            # 删掉L 挪窗口
            if grumpy[left] == 1:
                curt_sum -= customers[left]
            left += 1

        return max_sum


class Solution:
    """
    @param customers: the number of customers
    @param grumpy: the owner's temper every day
    @param X: X days
    @return: calc the max satisfied customers
    九章答案
    """

    def maxSatisfied(self, customers, grumpy, X):
        n = len(customers)
        satisfied_sum = 0

        # 先统计原本就给好评的人数
        for i in range(n):
            if grumpy[i] == 0:
                satisfied_sum += customers[i]

        # 记录最多的可能会变好评的人数
        max_become_satisfied = 0
        # 记录窗口中会变好评的人数
        become_satisfied = 0

        left = 0
        # 移动窗口的右端点
        for right in range(n):
            if grumpy[right] == 1:
                become_satisfied += customers[right]

            # 如果窗口中的个数过多，则移动左端点
            if right - left + 1 > X:
                if grumpy[left] == 1:
                    become_satisfied -= customers[left]
                left += 1

            max_become_satisfied = max(max_become_satisfied, become_satisfied)

        return satisfied_sum + max_become_satisfied