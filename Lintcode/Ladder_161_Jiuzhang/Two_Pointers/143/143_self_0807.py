class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    # 方法并不是最优
    def sortColors2(self, colors, k):
        if not colors:
            return None

        last_left = 0
        for i in range(1, k):
            last_left = self.twopartition(colors, i, last_left)

        return colors

    def twopartition(self, colors, color, start):
        left, right = start, len(colors) - 1
        while left <= right:
            while left <= right and colors[left] == color:
                left += 1
            while left <= right and colors[right] != color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        return left