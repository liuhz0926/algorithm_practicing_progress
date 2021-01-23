class Solution:
    """
    @param arr: the arr
    @return: the length of the longset subarray

    # 子数组问题，找最长的连续只有两个的子串

    """

    def pickFruits(self, arr):
        if not arr:
            return 0

        fruit_count = {}

        left = 0
        max_length = 0

        for right in range(len(arr)):
            # 移动right的时候如果没有超过3 就记录长度，加入后超过三了说明上一段结束了。就要开始移动left了
            fruit_count[arr[right]] = fruit_count.get(arr[right], 0) + 1

            while left <= right and len(fruit_count) >= 3:
                fruit_count[arr[left]] -= 1
                if fruit_count[arr[left]] == 0:
                    del fruit_count[arr[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
