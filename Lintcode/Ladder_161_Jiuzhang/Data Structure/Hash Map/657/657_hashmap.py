# 用hashmap来记录插入的val：index
# 如果删除一个index。将数组的最后一个数字放到需要删除的数的位置上，删除数组最后一位，同时更新hashmap
# 插入就插入在数组最后一位，同时更新hashmap
# 随机根据数组的长度来获取随机一个index，然后根据index获取value
# 需要hashmap来级的index的原因是因为pop的时候，不知道是删除的第几位。然后我们不能是index为0123，删除了2 在013里面random
# 所以hashmap的作用是删除的时候锁定index是多少，然后把最后一位3上的放在2上，这样删除最后一个3，最后random 012 就行了
# hashmap, val : index这种写法经常和数组list对应的写，来通过value来找index

import random


class RandomizedSet:

    def __init__(self):
        # do intialization if necessary
        self.nums, self.val_to_index = [], {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """

    def insert(self, val):
        # 包含了，不重复，return false
        if val in self.val_to_index:
            return False
        # 放到最后
        self.nums.append(val)
        self.val_to_index[val] = len(self.val_to_index)
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val):
        # 元素不存在，返回false
        if val not in self.val_to_index:
            return False

        # 先找到这个数字对应的index
        index = self.val_to_index[val]
        # 要和last进行替换
        last = self.nums[-1]

        # move the last element to index
        self.nums[index] = last
        self.val_to_index[last] = index

        # 删除数组最后一个val和删除这个val在hashmap里面
        self.nums.pop()
        del self.val_to_index[val]
        return True

    """
    @return: Get a random element from the set
    """

    def getRandom(self):
        # 根据数组长度来random
        return self.nums[random.randint(0, len((self.nums)) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()