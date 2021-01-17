class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """

    def minWindow(self, source, target):
        if not source:
            return ""

        # 提取target字母次数
        target_to_count = self.count_target(target)
        source_to_count = {}
        matched_size = 0
        left = 0
        sub_start, sub_length = 0, float('inf')

        for right in range(len(source)):
            # 不match不记录
            if source[right] not in target_to_count:
                continue

            # match的单词，记录，相等了+1
            source_to_count[source[right]] = source_to_count.get(source[right], 0) + 1
            if source_to_count[source[right]] == target_to_count[source[right]]:
                matched_size += 1

            while left <= right and matched_size == len(target_to_count):
                # match了，开始移动left，先打擂台记录最小的情况
                if right - left + 1 < sub_length:
                    sub_start, sub_length = left, right - left + 1

                # 对应前面不记录不在里面的单词
                if source[left] not in target_to_count:
                    left += 1
                    continue

                # 当有这个单词且目前的size刚好是target里的时候，matchsize -1
                if source_to_count[source[left]] == target_to_count[source[left]]:
                    matched_size -= 1
                source_to_count[source[left]] -= 1
                left += 1

        if sub_length == float('inf'):
            return ""
        return source[sub_start: sub_start + sub_length]

    def count_target(self, target):
        target_to_count = {}
        for char in target:
            target_to_count[char] = target_to_count.get(char, 0) + 1
        return target_to_count