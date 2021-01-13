class Solution:
    """
    @param nums: An array of integers
    @return: An integer

    answer: https://www.jiuzhang.com/solution/maximum-product-subarray/

    """

    def maxProduct(self, nums):
        if not nums:
            return None

        global_max = prev_max = prev_min = nums[0]
        for num in nums[1:]:
            # 如果是正的
            if num > 0:
                # max可能是前面的数字最大product乘以当前的，但也有可能没有当前的大
                # 比如：-1，2，4，1前面俩。2自己比-2的product大
                curt_max = max(num, prev_max * num)
                # min同理
                curt_min = min(num, prev_min * num)
            # 如果是负的
            else:
                # max是前面的最小值加了符号，有可能是最大。
                curt_max = max(num, prev_min * num)
                # min是前面最大反过来
                curt_min = min(num, prev_max * num)

            # 在current里的max 记录是不是global最大。然后替换下一组
            global_max = max(global_max, curt_max)
            prev_max, prev_min = curt_max, curt_min

        return global_max