class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair

    方法其实还是相向双指针，把L和R找到下一个位置不是++1
    """

    def twoSumVII(self, nums, target):
        if not nums:
            return []

        left, right = 0, 0

        # 先找到最小值和最大值，不断地和L和R比较
        for i in range(len(nums)):
            if nums[i] > nums[right]:
                right = i
            if nums[i] < nums[left]:
                left = i

        result = []
        # 相向双指针移动
        while nums[left] < nums[right]:
            curt_sum = nums[left] + nums[right]
            if curt_sum < target:
                left = self.next_left(nums, left)
                # -1了没答案了break
                if left == -1:
                    break
            elif curt_sum > target:
                right = self.next_right(nums, right)
                if right == -1:
                    break
            else:
                # 就两个直接sort
                result.append(sorted([left, right]))
                # 继续移动
                left = self.next_left(nums, left)
                if left == -1:
                    break

        return result

    def next_left(self, nums, left):
        # 判断当前是不是负的
        if nums[left] < 0:
            # 负数还没走到头
            for i in range(left - 1, -1, -1):
                if nums[i] < 0:
                    return i
            # 负数走到头
            for i in range(len(nums)):
                if nums[i] >= 0:
                    return i
        # 当前不是负的
        else:
            for i in range(left + 1, len(nums)):
                # 找下一个非负的
                if nums[i] >= 0:
                    return i
        # 都到头了
        return -1

    def next_right(self, nums, right):
        # 判断当前是不是正的
        if nums[right] > 0:
            # 正数还没走到头
            for i in range(right - 1, -1, -1):
                if nums[i] > 0:
                    return i
            # 正数走到头
            for i in range(len(nums)):
                if nums[i] <= 0:
                    return i
        # 当前不是正的
        else:
            for i in range(right + 1, len(nums)):
                # 找下一个非正的
                if nums[i] <= 0:
                    return i
        # 都到头了
        return -1