class TwoSum:

    def __init__(self):
        self.nums = []

    def add(self, number):
        # 先把新的加在最后
        self.nums.append(number)
        # 新加的index
        index = len(self.nums) - 1
        # 只要当前面的数字大于当前数字。把前面的数字往后调（所以最多情况为O(n)
        while index > 0 and self.nums[index - 1] > self.nums[index]:
            temp = self.nums[index - 1]
            self.nums[index - 1] = self.nums[index]
            self.nums[index] = temp
            index -= 1

    def find(self, value):
        # 正常二分法
        left, right = 0, len(self.nums) - 1
        while left < right:
            two_sum = self.nums[left] + self.nums[right]
            if two_sum < value:
                left += 1
            elif two_sum > value:
                right -= 1
            else:
                return True
        return False