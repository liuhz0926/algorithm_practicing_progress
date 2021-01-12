class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        # write your code here
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:  # right不是0
                if left != right:  # 其实可以不加这个条件。因为这样无非就是自己等自己罢了。但是这个方法可以降低最小的写次数
                    # 不重合， left要代表所有走过的非0数的顺序。所以如果两者重合。且他不是0。那就得让left往前走
                    nums[left] = nums[right]
                left += 1
            right += 1

        while left < len(nums):
            # right到头之后left把剩下的数字全部改成0
            if nums[left] != 0:
                nums[left] = 0
            left += 1
