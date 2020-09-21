class LinkedNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


# 方法类似LRU

class DataStream:

    def __init__(self):
        self.dummy = LinkedNode()
        # 头结点是first 后面的都是加在后面
        self.tail = self.dummy
        self.num_to_prev = {}
        # 记录存在duplicate的num，这样的num不会再linkedlist里面
        self.duplicates = set()

    """
    @param num: next number in stream
    @return: nothing
    """

    def add(self, num):
        # 看看是不是出现过，而且已经有至少两个了
        if num in self.duplicates:
            return

        # 新来的，没有出现过的，用pushback直接加在最后
        if num not in self.num_to_prev:
            self.push_back(num)
            return

            # 出现过，但是只有一个，没有在duplicate里面，所以要给他删除，然后放在duplicate里
        self.remove(num)
        self.duplicates.add(num)

    def push_back(self, num):
        # new num add to the tail 新来的都加在后面
        self.tail.next = LinkedNode(num)
        self.num_to_prev[num] = self.tail
        self.tail = self.tail.next

    def remove(self, num):
        # remove node for num (in the case of duplicate, we don't want it)
        prev = self.num_to_prev[num]

        # 把num对应的点删掉
        del self.num_to_prev[num]
        prev.next = prev.next.next
        # 看prev是不是tail，tail是其他数字那就在hashmap里面更新下
        if prev.next:
            self.num_to_prev[prev.next.value] = prev
        else:
            # if we removed the tail node, prev will be the new tail (num对应的是原来的tail)
            self.tail = prev

    """
    @return: the first unique number in stream
    """

    def firstUnique(self):
        # 看头结点有没有，要是没有直接return number
        if not self.dummy.next:  # 必须这么写要不next是none，none没有none.value
            return None
        return self.dummy.next.value


