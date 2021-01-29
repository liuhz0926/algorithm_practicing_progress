class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    法1 set
    """
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        intersec = set()
        for num in set1:
            if num in set2:
                intersec.add(num)
        return list(intersec)


class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    法2：同向双指针
    """

    def intersection(self, nums1, nums2):
        set1 = sorted(nums1)
        set2 = sorted(nums2)

        i, j = 0, 0
        res = set()
        while i < len(set1) and j < len(set2):
            if set1[i] == set2[j]:
                res.add(set1[i])
                i += 1
                j += 1
            elif set1[i] < set2[j]:
                i += 1
            else:
                j += 1

        return list(res)


class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array

    法3 二分查找
    """

    def intersection(self, nums1, nums2):
        sorted_num1 = sorted(nums1)

        res = set()
        for num in nums2:
            if self.is_in_nums(sorted_num1, num):
                res.add(num)

        return list(res)

    def is_in_nums(self, nums, target):
        if not nums:
            return False

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target or nums[end] == target:
            return True
        return False
