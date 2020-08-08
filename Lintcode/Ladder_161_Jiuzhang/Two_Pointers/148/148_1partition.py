class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):
        # write your code here
        # index从左到右一个一个挪一直移动 left只管0，right只管2
        left, index, right = 0, 0, len(nums) - 1
        # 注意这里是等到index遇到right的时候。
        while index <= right:
            # index遇到0， 和left当前的替换，把0全都扔到left区域去
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            # index 遇到2， 和right当前替换，right往前挪一位，但是i不变。如果index一直遇到的是2，则会一直把2替换到right上面
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
            else:  # 1的情况。skip过去
                index += 1

        return nums
