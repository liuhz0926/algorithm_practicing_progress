class Solution:
    """
    @param stops: An array represents where each car stops.
    @param k: The number of cars should be covered.
    @return: return the minimum length of the shed that meets the requirements.
    """

    def calculate(self, stops, k):

        # edge case:里面只有k辆车，所以for loop无法进入，直接return k
        if k == len(stops):
            return k

        sorted_stops = sorted(stops)

        # 贪心思维：考虑至少cover k辆车，其实是看她刚好差一丢丢cover到k+1辆车。
        min_length = 0
        for left in range(len(stops) - k):
            # cover到left但是cover不到left + k 差一格
            curt_spot = sorted_stops[left]
            # 查一格cover到后面的第k辆车（left和k之间差了k+1辆）
            right_spot = sorted_stops[left + k] - 1
            # 打擂台: 距离是右边-左边+1(因为index)
            min_length = max(min_length, right_spot - curt_spot + 1)

        return min_length
