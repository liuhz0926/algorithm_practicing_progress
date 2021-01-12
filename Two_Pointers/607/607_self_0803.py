class TwoSum:

    def __init__(self):
        self.numbers = []

    """
    @param number: An integer
    @return: nothing
    """

    def add(self, number):
        # write your code here
        self.numbers.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        if not self.numbers:
            return False

        nums = sorted(self.numbers)

        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < value:
                left += 1
            elif nums[left] + nums[right] > value:
                right -= 1
            else:
                return True

        return False