class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """

    def minWindow(self, source, target):
        if not source:
            return ""

        target_to_count = self.count_target(target)
        source_to_count = {}
        left, right = 0, 0
        matched_size = 0
        sub_start, sub_length = 0, float('inf')

        while left < len(source) and right < len(source):

            while right < len(source) and matched_size < len(target_to_count):
                # 挪right，match的还没有全部的词语
                # 不记录没出现在target的
                if source[right] not in target_to_count:
                    right += 1
                    continue
                # 等于target的了matchsize+1
                source_to_count[source[right]] = source_to_count.get(source[right], 0) + 1
                if source_to_count[source[right]] == target_to_count[source[right]]:
                    matched_size += 1
                right += 1

            while left <= right and matched_size == len(target_to_count):
                # 记录长度
                if right - left < sub_length:
                    sub_start, sub_length = left, right - left

                # 挪left
                # 出现在target的跳过
                if source[left] not in target_to_count:
                    left += 1
                    continue
                # 删除前刚好相等，所以先-1 （也可以放在sourcetocount-=1 后 这样等于target里的-1）
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
        return target_to_countv