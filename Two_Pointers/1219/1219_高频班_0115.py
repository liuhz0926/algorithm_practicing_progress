class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    二分答案+暴力找
    """

    def findRadius(self, houses, heaters):
        left, right = 0, 10 ** 9

        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.can_heat_all(houses, heaters, mid):
                right = mid
            else:
                left = mid

        # 最后找到锁定的mid后，因为下雨等于所以先看left
        if self.can_heat_all(houses, heaters, left):
            return left
        return right

    def can_heat_all(self, houses, heaters, k):
        for house in houses:
            can_heat = False
            for heater in heaters:
                # house和heater之间小于等于k，可以加热
                if abs(heater - house) <= k:
                    can_heat = True
                    break
            # 这个house无法加热直接返回
            if not can_heat:
                return False
        # 全都可以
        return True


class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    二分答案+同向双指针找heat all
    """

    def findRadius(self, houses, heaters):
        # 双指针前提！排序
        houses = sorted(houses)
        heaters = sorted(heaters)

        left, right = 0, 10 ** 9

        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.can_heat_all(houses, heaters, mid):
                right = mid
            else:
                left = mid

        # 最后找到锁定的mid后，因为下雨等于所以先看left
        if self.can_heat_all(houses, heaters, left):
            return left
        return right

    def can_heat_all(self, houses, heaters, k):
        # 用同向双指针来确定是否可以都加热
        i, j = 0, 0

        while i < len(houses) and j < len(heaters):
            # 可以加热
            if abs(houses[i] - heaters[j]) <= k:
                i += 1
            # 不可以加热 (因为这个够不到当前的了，所以换下一个)
            else:
                j += 1
        # 最后看i有没有到达houses最后，到达了说明都加热了 （最后是n-1）
        return i == len(houses)


class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    二分法 找每个房屋的最近的heater

    """

    def findRadius(self, houses, heaters):
        # 二分法，双指针都是建立在排序基础上的
        heaters = sorted(heaters)
        res_radius = 0
        for house in houses:
            # 查找每一个house放入heaters的位置
            radius = self.find_closest_heater(heaters, house)
            # 结果的k是所有的radius里面的最大值是最小能让所有heaters的值
            res_radius = max(res_radius, radius)
        return res_radius

    def find_closest_heater(self, heaters, target):
        # 二分查找target插入heaters的位置
        left, right = 0, len(heaters) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if heaters[mid] >= target:
                right = mid
            else:
                left = mid

        # 选取更近的heater（最后找到插入left target right，看哪个更近）
        left_dist = abs(heaters[left] - target)
        right_dist = abs(heaters[right] - target)
        return min(left_dist, right_dist)


class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    同向双指针：和ppt的四点有些不同

    """

    def findRadius(self, houses, heaters):
        # 双指针要sort
        houses = sorted(houses)
        heaters = sorted(heaters)
        i, j = 0, 0
        res_radius = 0

        while i < len(houses) and j < len(heaters):
            curt_radius = abs(houses[i] - heaters[j])
            next_radius = float('inf')
            # 否则越界，只有还没到最后的时候，计算和j+1的距离
            if j < len(heaters) - 1:
                next_radius = abs(houses[i] - heaters[j + 1])
            # 只有i和j匹配上的时候i要往前移动
            if curt_radius < next_radius:
                res_radius = max(res_radius, curt_radius)
                i += 1
            # 一旦i要跟j+1或者更后面，都要优先移动j
            else:
                j += 1

        return res_radius


class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """

    def findRadius(self, houses, heaters):
        houses = sorted(houses)
        heaters = sorted(heaters)
        i, j = 0, 0
        res_radius = 0

        while i < len(houses) and j < len(heaters):

            curt_radius = abs(heaters[j] - houses[i])

            # j还没到头
            if j < len(heaters) - 1:

                # i在前面或者中间
                if houses[i] < heaters[j + 1]:
                    next_radius = abs(heaters[j + 1] - houses[i])
                    res_radius = max(res_radius, min(curt_radius, next_radius))
                    i += 1
                # i在后面
                else:
                    j += 1

            # j 到头了
            else:
                res_radius = max(res_radius, curt_radius)
                i += 1

        return res_radius


