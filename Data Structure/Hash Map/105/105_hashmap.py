"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # O(n)的方法
        # copy的方法是，用hashmap对应 原node ： copy node
        # 循环两次第一次copy 所有的点，第二次复制关系，next和random关系
        # 必须循环两次是因为如果有的点不在hashmap里面，所以没法copy
        original_to_copy = dict()
        # 第一次copy所有点
        original = head
        while original:
            original_to_copy[original] = RandomListNode(original.label)
            original = original.next

        # 第二次copy所有关系
        original = head
        while original:
            if original.next:
                original_to_copy[original].next = original_to_copy[original.next]
            if original.random:
                original_to_copy[original].random = original_to_copy[original.random]
            original = original.next

        return original_to_copy[head]