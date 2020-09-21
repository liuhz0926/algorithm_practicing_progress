# 九章上Su的答案
# 利用linkedlist把一样的value串起来。一个open hash的方法

import random


class LinkedListNode(object):

    def __init__(self, val=None):
        self.val = val
        self.nxt = None


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val2nodes = dict()
        self.nodes = list()
        self.node2index = dict()

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        is_new = val not in self.val2nodes
        node = LinkedListNode(val)
        self.nodes.append(node)
        self.node2index[node] = len(self.nodes) - 1
        if is_new:
            self.val2nodes[val] = node
            return True
        else:
            existed_nodes = self.val2nodes[val]
            node.nxt = existed_nodes
            self.val2nodes[val] = node
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if (not (val in self.val2nodes)):
            return False

        head_old = self.val2nodes[val]
        self.val2nodes[val] = head_old.nxt
        if (self.val2nodes[val] == None):
            self.val2nodes.pop(val)
        index = self.node2index[head_old]
        last_node = self.nodes[-1]
        self.nodes[index] = last_node
        self.nodes.pop(-1)
        self.node2index[last_node] = index
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        index = random.randrange(len(self.nodes))
        node = self.nodes[index]
        return node.val

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()